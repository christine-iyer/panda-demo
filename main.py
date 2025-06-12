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