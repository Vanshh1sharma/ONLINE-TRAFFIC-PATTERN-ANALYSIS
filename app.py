import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
import requests
import geopandas as gpd
from shapely.geometry import LineString

# -----------------------
# Page Config
# -----------------------
st.set_page_config(
    page_title="Delhi Smart Traffic Route Planner",
    page_icon="🚦",
    layout="wide"
)

st.title("🚦 Delhi Smart Traffic Route Planner")

# -----------------------
# Load Traffic Dataset
# -----------------------
@st.cache_data
def load_data():
    traffic_data = gpd.read_file(
        "dataset/new_delhi__2024-08-12_to_2024-08-12_.geojson"
    )

    def extract_probe_counts(x):
        if isinstance(x, list):
            return sum(i.get("probeCount", 0) for i in x)
        return 0

    traffic_data["traffic_volume"] = traffic_data["segmentProbeCounts"].apply(
        extract_probe_counts
    )

    return traffic_data

traffic_data = load_data()

# -----------------------
# Geocoder
# -----------------------
geolocator = Nominatim(user_agent="traffic_app")

def get_coordinates(place):
    try:
        location = geolocator.geocode(place)
        if location:
            return (location.latitude, location.longitude)
    except:
        return None

# -----------------------
# OSRM Routing (Driving Only)
# -----------------------
def get_routes(start_coords, dest_coords):

    url = f"http://router.project-osrm.org/route/v1/driving/{start_coords[1]},{start_coords[0]};{dest_coords[1]},{dest_coords[0]}?alternatives=true&overview=full&geometries=geojson"

    response = requests.get(url)
    data = response.json()

    routes = []

    if "routes" not in data:
        return []

    for route in data["routes"]:
        distance = route["distance"] / 1000
        duration = route["duration"] / 60

        coordinates = route["geometry"]["coordinates"]
        route_points = [(coord[1], coord[0]) for coord in coordinates]

        routes.append({
            "distance": distance,
            "duration": duration,
            "geometry": route_points
        })

    return routes

# -----------------------
# UI Inputs
# -----------------------
col1, col2 = st.columns(2)

with col1:
    start = st.text_input("Enter Starting Location")

with col2:
    destination = st.text_input("Enter Destination")

if "route_data" not in st.session_state:
    st.session_state.route_data = None

# -----------------------
# Calculate Route
# -----------------------
if st.button("Calculate Route"):

    start_coords = get_coordinates(start)
    dest_coords = get_coordinates(destination)

    if start_coords and dest_coords:

        routes = get_routes(start_coords, dest_coords)

        if len(routes) == 0:
            st.error("❌ No route found")
            st.stop()

        # Sort routes by time (fastest first)
        routes = sorted(routes, key=lambda x: x["duration"])

        best_route = routes[0]
        alt_route = routes[1] if len(routes) > 1 else None

        # Traffic label (only for best route)
        route_line = LineString(best_route["geometry"])

        nearby_roads = traffic_data[
            traffic_data.geometry.distance(route_line) < 0.001
        ]

        if len(nearby_roads) > 0:
            route_volume = nearby_roads["traffic_volume"].mean()
        else:
            route_volume = traffic_data["traffic_volume"].mean()

        if route_volume > 1000:
            traffic = "🔴 High Traffic"
        elif route_volume > 300:
            traffic = "🟠 Moderate Traffic"
        else:
            traffic = "🟢 Low Traffic"

        st.session_state.route_data = {
            "start": start_coords,
            "dest": dest_coords,
            "best": best_route,
            "alt": alt_route,
            "traffic": traffic
        }

    else:
        st.error("❌ Location not found")

# -----------------------
# Display Results
# -----------------------
if st.session_state.route_data:

    data = st.session_state.route_data

    st.subheader("🚀 Best Route")

    st.success(f"Distance: {round(data['best']['distance'],2)} km")
    st.success(f"Time: {round(data['best']['duration'],1)} minutes")
    st.write("Traffic:", data["traffic"])

    if data["alt"]:
        st.subheader("🔁 Alternative Route")

        st.info(f"Distance: {round(data['alt']['distance'],2)} km")
        st.info(f"Time: {round(data['alt']['duration'],1)} minutes")

    else:
        st.write("No alternative route available")

    # -----------------------
    # Map
    # -----------------------
    m = folium.Map(location=data["start"], zoom_start=12)

    folium.Marker(
        data["start"],
        popup="Start",
        icon=folium.Icon(color="green")
    ).add_to(m)

    folium.Marker(
        data["dest"],
        popup="Destination",
        icon=folium.Icon(color="red")
    ).add_to(m)

    # Best Route
    folium.PolyLine(
        data["best"]["geometry"],
        color="green",
        weight=7,
        tooltip="🚀 Best Route"
    ).add_to(m)

    # Alternative Route
    if data["alt"]:
        folium.PolyLine(
            data["alt"]["geometry"],
            color="blue",
            weight=4,
            opacity=0.6,
            tooltip="Alternative Route"
        ).add_to(m)

    st_folium(m, height=600, use_container_width=True)

else:
    m = folium.Map(location=[28.6139, 77.2090], zoom_start=11)
    st_folium(m, height=600, use_container_width=True)