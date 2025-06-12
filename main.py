import pandas as pd
file_path="democracy-index-eiu/democracy-index-eiu.csv"
data= pd.read_csv(file_path, encoding='latin1')
print(data.head())