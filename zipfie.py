import pandas as pd
import zipfile
import os

# Path to the zip file
zip_file_path = "/Users/christineiyer/Documents/chez-le-weekend/democracy/democracy-index-eiu/democracy-index-eiu.zip"
# Extract the contents of the zip file
extracted_folder = "democracy-index-eiu/extracted_data"
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder)

# List all CSV files in the extracted folder
csv_files = [f for f in os.listdir(extracted_folder) if f.endswith('.csv')]

# Process each CSV file
for csv_file in csv_files:
    file_path = os.path.join(extracted_folder, csv_file)
    print(f"Processing file: {file_path}")
    
    # Load the CSV file
    data = pd.read_csv(file_path, encoding='latin1')
    
    # Inspect the data
    print(data.head())
    print(data.info())
    
    # Handle missing values
    data = data.dropna()
    
    # Rename columns (example: rename 'Entity' to 'Country')
    if "Entity" in data.columns:
        data = data.rename(columns={"Entity": "Country", "Code": "CountryCode"})
    
    # Filter rows (example: select rows where Year is greater than 2000)
    if "Year" in data.columns:
        data = data[data["Year"] > 2000]
    
    # Transform data (example: normalize the Democracy score column)
    if "Democracy score" in data.columns:
        data["Democracy score"] = data["Democracy score"] / 10
    
    # Save the cleaned data
    cleaned_file_path = os.path.join(extracted_folder, f"cleaned_{csv_file}")
    data.to_csv(cleaned_file_path, index=False)
    print(f"Cleaned data saved to {cleaned_file_path}")

    