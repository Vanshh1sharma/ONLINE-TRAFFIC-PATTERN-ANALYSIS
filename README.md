# 🚦 Delhi Smart Traffic Route Planner

## 📌 Project Overview

The **Delhi Smart Traffic Route Planner** is a web-based application that analyzes historical traffic data and provides route planning with congestion-aware travel time estimation.

The system integrates **traffic pattern analysis with road routing** to estimate travel times and suggest alternative routes based on congestion levels.

The project uses **traffic probe data from Delhi** and combines it with **OpenStreetMap routing services** to create a traffic-aware navigation prototype.



## 🎯 Objectives

The main objectives of this project are:

- Analyze historical traffic patterns in Delhi.
- Identify congested road segments.
- Estimate travel time based on traffic conditions.
- Provide route planning between two locations.
- Suggest alternative routes when congestion is high.
- Visualize traffic patterns using interactive maps.



## ⚙️ Technologies Used

| Technology | Purpose |
|------------|--------|
| Python | Core programming language |
| Streamlit | Web interface |
| Folium | Interactive map visualization |
| GeoPandas | Geospatial data processing |
| OSRM API | Road routing engine |
| Geopy | Geolocation and distance calculation |
| Shapely | Spatial geometry analysis |
| Pandas | Data analysis |
| Matplotlib | Traffic visualization |



## 📊 Dataset

The project uses the **New Delhi Traffic Probe Count Dataset (2024)**.

This dataset includes:

- Road segment geometry
- Vehicle probe counts
- Time ranges
- Traffic intensity data

The dataset helps identify **historical congestion patterns** on Delhi roads.

Example file:


dataset/new_delhi__2024-08-12_to_2024-08-12_.geojson


Traffic volume is calculated from:


segmentProbeCounts



## 🚀 Key Features

### 1️⃣ Traffic Pattern Analysis

The system analyzes traffic probe counts to determine:

- Busiest roads
- Traffic distribution
- Congestion hotspots

---

### 2️⃣ Traffic Classification

Roads are categorized into traffic levels:

| Traffic Volume | Level |
|----------------|------|
| High volume | High Traffic |
| Medium volume | Moderate Traffic |
| Low volume | Low Traffic |

---

### 3️⃣ Route Planning

Users can enter:


Start Location
Destination


The system calculates:

- Driving route
- Travel distance
- Estimated travel time



### 4️⃣ Traffic-Aware Travel Time

The route travel time is adjusted based on **traffic congestion patterns from the dataset**.

Higher congestion leads to **lower assumed speed and longer travel time**.

---

### 5️⃣ Alternative Route Suggestion

If multiple routes exist, the system shows:

- Main route
- Alternative route

This helps users avoid congested roads.

---

### 6️⃣ Interactive Map Visualization

The application displays:

- Start location
- Destination
- Main route
- Alternative route
- Traffic congestion levels

Using an interactive map interface.

---

## 🗂 Project Structure


TRAFFIC_PROJECT
│
├── dataset
│ └── new_delhi__2024-08-12_to_2024-08-12_.geojson
│
├── analysis
│ ├── analysis.py
│ ├── traffic_map.py
│ ├── graph.py
│ └── distribution_graph.py
│
├── app.py
├── requirements.txt
├── README.md
│
├── archive
└── venv


---

## 🖥 How to Run the Project

### 1️⃣ Clone the Repository


git clone https://github.com/YOURUSERNAME/delhi-traffic-route-planner.git


---

### 2️⃣ Navigate to the Project Folder


cd delhi-traffic-route-planner


---

### 3️⃣ Install Dependencies


pip install -r requirements.txt


---

### 4️⃣ Run the Application


streamlit run app.py


The web application will open in your browser.

---

## 📍 Example Usage

Input:


Start: India Gate Delhi
Destination: Sadar Bazar Delhi


Output:

- Route map
- Estimated distance
- Travel time
- Traffic level
- Alternative route suggestion



## 📈 Future Improvements

Possible extensions include:

- Integration with real-time traffic APIs
- Machine learning-based congestion prediction
- Traffic simulation models
- Multi-city support
- Mobile application interface



## 📜 Conclusion

This project demonstrates how **traffic data analysis and routing systems can be combined to support smarter urban mobility planning**.

By using historical traffic patterns and geospatial analysis, the system provides traffic-aware route recommendations that help users plan travel more efficiently.



## 👨‍💻 Author

Developed as part of a **Traffic Pattern Analysis and Route Planning Project**.