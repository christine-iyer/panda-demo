import pandas as pd
file_path="democracy-index-eiu/democracy-index-eiu.csv"
data= pd.read_csv(file_path, encoding='latin1')
print(data.head())
print(data.info())
# Display the first few rows of the DataFrame
print(data.describe())
# Display the column names
print(data.columns)
data = data.dropna()
# Rename columns (example: rename 'Entity' to 'Country')
data = data.rename(columns={"Entity": "Country", "Code": "CountryCode"})

data = data[data["Year"] > 2000]
print(data.head())

# Transform data...normalize the democracy score
if "Democracy score" in data.columns:
     data["Democracy score"] = data["Democracy score"] / 10

print(data.head())    

# Save the new data
output_path = 'democracy-index-eiu/cleaned_democracy_index.csv'
data.to_csv(output_path, index=False)
print(f"Cleaned data saved to {output_path}")

#Read in the data in the zip file
import zipfile
zip_file_path = "democracy-index-eiu/democracy-index-eiu.zip"    
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall("democracy-index-eiu/extracted_data")
# Read the extracted CSV file
extracted_file_path = "democracy-index-eiu/extracted_data/democracy_index.csv"
extracted_data = pd.read_csv(extracted_file_path, encoding='latin1')
print(extracted_data.head())