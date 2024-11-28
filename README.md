# Event-Search
## Overview

The Event Search and Statistics Dashboard is a comprehensive web application that allows users to explore, filter, and visualize event data stored in Elasticsearch. It features a search functionality for finding specific events and a statistics section for visualizing event trends. The data used for this project includes around 1000 events across the USA, sourced from the Ticketmaster API.

## Features

Search Events: <br/>
	• Filter events by city, genre, and price range. <br/>
	• Display event details such as name, date, time, venue, genre, and price range. <br/>
	• Open event URLs directly for more information. <br/>
 
Event Statistics: <br/>
	• Visualize the total events by city and genre. <br/>
	• Display month vs. city-wise event trends. <br/>
	• Interactively filter statistics by city and genre. <br/>

## Requirements

1.	Python: Version 3.10 or higher 
2.	Elasticsearch: Version 8.x <br/>
       • Ports Used: <br/>
   	Elasticsearch is configured to run on 192.168.0.59 at port 9200. <br/>
   	Backend Flask application runs on http://127.0.0.1:5000. <br/>
   	Frontend Streamlit application runs on http://localhost:8501. <br/>
4.	Libraries: <br/>
   	• streamlit <br/>
   	• flask <br/>
   	• requests <br/>
   	• pandas <br/>
   	• plotly <br/>
   	• elasticsearch <br/>

## Step-by-Step Instructions

1. Download and Install Elasticsearch <br/>

	•	Download: Elasticsearch Official Website <br/>
	•	Start Elasticsearch: <br/>
	•	Unzip the downloaded Elasticsearch package. <br/>
	•	Navigate to the bin directory and run: <br/>

```
./elasticsearch
```
2. Load Data into Elasticsearch

	•	Open the file load_to_es.py and ensure your Elasticsearch host and port (192.168.0.59:9200) are correct. <br/>
	•	This script includes: <br/>
	•	Defining the index mapping for the events3 index. <br/>
	•	Loading Ticketmaster API data of around 1000 events into Elasticsearch. <br/>
	•	Run the script: <br/>
```
python load_to_es.py
```

3. Run the Backend Server

	•	The backend server handles API requests for filtering and fetching data from Elasticsearch. <br/>
	•	Open the file backend1.py and ensure the Elasticsearch host and port are correct. <br/>
	•	Run the backend: <br/>
```
python backend1.py
```
Verify the backend is running by accessing http://127.0.0.1:5000 in your browser.

4. Run the Frontend Application

	•	The frontend application is built using Streamlit and provides an interactive dashboard. <br/>
	•	Open the file frontend1.py. <br/>
	•	Run the frontend: <br/>
```
streamlit run frontend1.py
```

## Usage Instructions

1.	Search Events:
	•	Navigate to the Search tab. <br/>
	•	Apply filters for city, genre, and price range. (eg. City: Phoenix, Genre: Basketball)<br/>
	•	View filtered events with detailed information. <br/>
	•	Open event URLs by clicking the respective button. <br/>

2.	Event Statistics:
	•	Navigate to the Statistics tab. <br/>
	•	Use filters to refine visualizations by city or genre. <br/>
	•	Explore bar and pie charts for event distribution by city and genre. <br/>
	•	View month vs. city-wise event trends. <br/>

## Key Files

• load_to_es.py: Loads data into Elasticsearch and defines the mapping for the events3 index. <br/>
• backend1.py: Flask backend to interact with Elasticsearch for data filtering. <br/>
• frontend1.py: Streamlit frontend to search and visualize events. <br/>

## Technologies Used

• Elasticsearch: For data storage and querying. <br/>
• Flask: Backend API development. <br/>
• Streamlit: Interactive dashboard frontend. <br/>
• Plotly: Data visualization in the statistics section. <br/>

## Troubleshooting

• Elasticsearch Connection Error: Ensure Elasticsearch is running on 192.168.0.59:9200. <br/>
• Data Not Loaded: Run load_to_es.py to reload data into Elasticsearch. <br/>
• Frontend/Backend Issues: Check that Flask (backend1.py) and Streamlit (frontend1.py) applications are running without errors. <br/>
