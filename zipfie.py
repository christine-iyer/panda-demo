import pandas as pd
import requests

# Fetch the data
data_url = "https://ourworldindata.org/grapher/democracy-index-eiu.csv?v=1&csvType=full&useColumnShortNames=true"
df = pd.read_csv(data_url, storage_options={'User-Agent': 'Our World In Data data fetch/1.0'})

# Display the first few rows of the data
print("Data Preview:")
print(df.head())

# Display information about the data
print("\nData Info:")
print(df.info())

# Fetch the metadata
metadata_url = "https://ourworldindata.org/grapher/democracy-index-eiu.metadata.json?v=1&csvType=full&useColumnShortNames=true"
metadata = requests.get(metadata_url, headers={'User-Agent': 'Our World In Data data fetch/1.0'}, verify=False).json()

# Display the metadata
print("\nMetadata:")
print(metadata)