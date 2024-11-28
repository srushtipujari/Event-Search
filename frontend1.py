import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime

# Backend API endpoint
API_URL = "http://127.0.0.1:5000/filter"

common_path = "/Users/srushtipujari/Desktop/Bonus Project/Pictures/"

# Genre Images
GENRE_IMAGES = {
    "Basketball": common_path + "basketball.png",
    "Football": common_path + "football.png",
    "Hockey": common_path + "ice-hockey.png",
    "Theatre": common_path + "theater.png",
    "Ice Shows": common_path + "ice-skating.png",
    "Rock": common_path + "rock-n-roll.png",
    "Spectacular": common_path +  "concert.png"
}

DEFAULT_IMAGE = common_path + "people.png"  # A generic fallback image

# App Title
st.title("Event Search Across USA")

# Load data from Elasticsearch
@st.cache_data
def load_data():
    # Send an empty filter to get all data
    response = requests.post(API_URL, json={})
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        st.error("Failed to load data from backend.")
        return pd.DataFrame()

# Load data
data = load_data()


# Tabs for Search and Statistics
tab1, tab2 = st.tabs(["Search", "Statistics"])

# --- SEARCH TAB ---
with tab1:
    st.header("Search Events")
    
    # Sidebar: Filters
    st.sidebar.header("Search Filters")
    
    # Filter by City
    city = st.sidebar.text_input("City", placeholder="Enter a city name", key="search_city")
    #city = st.sidebar.multiselect("Filter by City", data["City"].unique(), key="search_city")
    
    # Filter by Genre
    genre_options = list(GENRE_IMAGES.keys())
    genre = st.sidebar.selectbox("Genre", [""] + genre_options, key="search_genre")
    
    # Price range filter
    price_min = st.sidebar.number_input("Minimum Price", min_value=0.0, value=0.0, key="search_price_min")
    price_max = st.sidebar.number_input("Maximum Price", min_value=0.0, value=1000.0, key="search_price_max")
    
    # Apply Filters Button
    if st.sidebar.button("Apply Filters", key="search_button"):
        # Prepare filters
        filters = {
            "city": city,
            "genre": genre,
            "price_min": price_min,
            "price_max": price_max
        }
        
        # Call backend API
        response = requests.post(API_URL, json=filters)
        
        if response.status_code == 200:
            results = response.json()
            st.subheader("Filtered Results")
            if results:
                for event in results:

                    genre_image = GENRE_IMAGES.get(event["Genre"], DEFAULT_IMAGE)  # Use a default image if genre is not found

                    # Create a horizontal layout
                    cols = st.columns([0.1, 0.9])  # Two columns: one for the image, one for the title and details
                    with cols[0]:
                        st.image(
                            genre_image,
                            width=40,  # Adjust icon size
                            use_container_width=False
                        )
                    with cols[1]:
                        st.markdown(f"### **{event['Name']}**")
                        st.markdown(f"""
                        - **Date**: {event['Date']}  
                        - **Time**: {event['Time']}  
                        - **Venue**: {event['Venue']}  
                        - **City**: {event['City']}  
                        - **Genre**: {event['Genre']}  
                        - **PriceRange**: {event['PriceRange']} {event['Currency']}
                        """)

                        st.markdown(f'<a href="{event["URL"]}" target="_blank">Visit Event Page</a>', unsafe_allow_html=True)
                        
            else:
                st.write("No results found.")
        else:
            st.error("Failed to fetch results. Check the backend service.")

# --- STATISTICS TAB ---
with tab2:
    st.header("Event Statistics")
    
    if not data.empty:
        # Sidebar: Filters
        st.sidebar.header("Statistics Filters")
        
        # Filter by City
        stat_city_filter = st.sidebar.multiselect("Filter by City", data["City"].unique(), key="stats_city")
        
        # Filter by Genre
        stat_genre_filter = st.sidebar.multiselect("Filter by Genre", data["Genre"].unique(), key="stats_genre")
        
        # Apply Filters
        stat_filtered_data = data.copy()
        if stat_city_filter:
            stat_filtered_data = stat_filtered_data[stat_filtered_data["City"].isin(stat_city_filter)]
        if stat_genre_filter:
            stat_filtered_data = stat_filtered_data[stat_filtered_data["Genre"].isin(stat_genre_filter)]
        
        # Display statistics
        st.sidebar.markdown("---")
        st.sidebar.markdown("### Data Summary")
        st.sidebar.write(f"Total Events: {len(stat_filtered_data)}")
        # st.sidebar.write(f"Unique Cities: {stat_filtered_data['City'].nunique()}")
        # st.sidebar.write(f"Unique Genres: {stat_filtered_data['Genre'].nunique()}")
        
        # 1. Events by City
        city_count = stat_filtered_data["City"].value_counts().reset_index()
        city_count.columns = ["City", "Event Count"]
        st.subheader("Total Events by City")
        fig_city = px.bar(city_count, x="City", y="Event Count", color="City", title="Events by City")
        st.plotly_chart(fig_city, use_container_width=True)
        
        # 2. Events by Genre
        genre_count = stat_filtered_data["Genre"].value_counts().reset_index()
        genre_count.columns = ["Genre", "Event Count"]
        st.subheader("Total Events by Genre")
        fig_genre = px.pie(genre_count, names="Genre", values="Event Count", title="Events by Genre")
        st.plotly_chart(fig_genre, use_container_width=True)
        
        # 3. Month vs. City-Wise Events
        stat_filtered_data["Month"] = pd.to_datetime(stat_filtered_data["Date"]).dt.month
        month_city_count = stat_filtered_data.groupby(["Month", "City"]).size().reset_index(name="Event Count")
        month_city_count["Month"] = month_city_count["Month"].apply(lambda x: datetime.strptime(str(x), "%m").strftime("%B"))
        st.subheader("Month vs. City-Wise Events")
        fig_month_city = px.bar(
            month_city_count,
            x="Month",
            y="Event Count",
            color="City",
            barmode="group",
            title="Month vs. City-Wise Events"
        )
        st.plotly_chart(fig_month_city, use_container_width=True)
        
        # 4. Raw Data Table
        st.subheader("Filtered Data Table")
        st.dataframe(stat_filtered_data)
    else:
        st.warning("No data available to display.")
