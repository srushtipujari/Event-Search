import pandas as pd
from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch([{'host': '192.168.0.59', 'port': 9200, 'scheme': 'http'}])

# Load the CSV file
file_path = 'all_events.csv'  # Replace with your CSV file path
df = pd.read_csv(file_path)


# Define cleaning functions
def clean_price(price):
    """Ensure price is a float or None for missing/invalid values."""
    try:
        return float(price) if pd.notnull(price) else None
    except:
        return None

def clean_currency(currency):
    """Ensure currency is a valid string or None for missing/invalid values."""
    return currency.strip() if pd.notnull(currency) else None

# Apply cleaning functions
df['PriceRange'] = df['PriceRange'].apply(clean_price)
df['Currency'] = df['Currency'].apply(clean_currency)

# Drop rows where PriceRange or Currency is missing
df.dropna(subset=['PriceRange', 'Currency'], inplace=True)

# Replace any remaining NaN values with None
df = df.where(pd.notnull(df), None)

# Define Elasticsearch index mapping
index_name = "events3"
index_mapping = {
    "mappings": {
        "properties": {
            "Name": {"type": "text"},
            "ID": {"type": "keyword"},
            "URL": {"type": "text"},
            "Date": {"type": "date", "format": "yyyy-MM-dd"},
            "Time": {"type": "text"},
            "Venue": {"type": "text"},
            "City": {"type": "text"},
            "Country": {"type": "text"},
            "Latitude": {"type": "float"},
            "Longitude": {"type": "float"},
            "Genre": {"type": "text"},
            "SubGenre": {"type": "text"},
            "PriceRange": {"type": "float"},
            "Currency": {"type": "keyword"}
        }
    }
}

# Create the index in Elasticsearch
if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)
    print(f"Deleted existing index '{index_name}'.")
es.indices.create(index=index_name, body=index_mapping)
print(f"Created index '{index_name}'.")

# Index data into Elasticsearch
for i, row in df.iterrows():
    doc = {
        "Name": row['Name'],
        "ID": row['ID'],
        "URL": row['URL'],
        "Date": row['Date'],
        "Time": row['Time'],
        "Venue": row['Venue'],
        "City": row['City'],
        "Country": row['Country'],
        "Latitude": row['Latitude'],
        "Longitude": row['Longitude'],
        "Genre": row['Genre'],
        "SubGenre": row['SubGenre'],
        "PriceRange": row['PriceRange'],
        "Currency": row['Currency']
    }
    try:
        es.index(index=index_name, id=i, body=doc)
    except Exception as e:
        print(f"Failed to index document {i}: {e}")

print("Data successfully loaded into Elasticsearch!")
