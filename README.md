# Event-Search
Overview

The Event Search and Statistics Dashboard is a comprehensive web application that allows users to explore, filter, and visualize event data stored in Elasticsearch. It features a search functionality for finding specific events and a statistics section for visualizing event trends.

Features

	•	Search Events:
	•	Filter events by city, genre, and price range.
	•	Display event details such as name, date, time, venue, genre, and price range.
	•	Open event URLs directly for more information.
	•	Event Statistics:
	•	Visualize the total events by city and genre.
	•	Display month vs. city-wise event trends.
	•	Interactively filter statistics by city and genre.

Requirements

	1.	Python: Version 3.10 or higher
	2.	Elasticsearch: Version 8.x
 	•	Ports Used:
	•	Elasticsearch is configured to run on 192.168.0.59 at port 9200.
	•	Backend Flask application runs on http://127.0.0.1:5000.
	•	Frontend Streamlit application runs on http://localhost:8501.
	3.	Libraries:
	•	streamlit
	•	flask
	•	requests
	•	pandas
	•	plotly
	•	elasticsearch

 Step-by-Step Instructions

1. Download and Install Elasticsearch

	•	Download: Elasticsearch Official Website
	•	Start Elasticsearch:
	•	Unzip the downloaded Elasticsearch package.
	•	Navigate to the bin directory and run:

```
./elasticsearch
```
2. Load Data into Elasticsearch

	•	Open the file load_to_es.py and ensure your Elasticsearch host and port (192.168.0.59:9200) are correct.
	•	This script includes:
	•	Defining the index mapping for the events3 index.
	•	Loading event data into Elasticsearch.
	•	Run the script:
```
python load_to_es.py
```

3. Run the Backend Server

	•	The backend server handles API requests for filtering and fetching data from Elasticsearch.
	•	Open the file backend1.py and ensure the Elasticsearch host and port are correct.
	•	Run the backend:
```
python backend1.py
```
	•	Verify the backend is running by accessing http://127.0.0.1:5000 in your browser.

4. Run the Frontend Application

	•	The frontend application is built using Streamlit and provides an interactive dashboard.
	•	Open the file frontend1.py.
	•	Run the frontend:
```
streamlit run frontend1.py
```

Usage Instructions

	1.	Search Events:
	•	Navigate to the Search tab.
	•	Apply filters for city, genre, and price range.
	•	View filtered events with detailed information.
	•	Open event URLs by clicking the respective button.
	2.	Event Statistics:
	•	Navigate to the Statistics tab.
	•	Use filters to refine visualizations by city or genre.
	•	Explore bar and pie charts for event distribution by city and genre.
	•	View month vs. city-wise event trends.

Key Files

	•	load_to_es.py: Loads data into Elasticsearch and defines the mapping for the events3 index.
	•	backend1.py: Flask backend to interact with Elasticsearch for data filtering.
	•	frontend1.py: Streamlit frontend to search and visualize events.

Technologies Used

	•	Elasticsearch: For data storage and querying.
	•	Flask: Backend API development.
	•	Streamlit: Interactive dashboard frontend.
	•	Plotly: Data visualization in the statistics section.

Troubleshooting

	•	Elasticsearch Connection Error: Ensure Elasticsearch is running on 192.168.0.59:9200.
	•	Data Not Loaded: Run load_to_es.py to reload data into Elasticsearch.
	•	Frontend/Backend Issues: Check that Flask (backend1.py) and Streamlit (frontend1.py) applications are running without errors.
