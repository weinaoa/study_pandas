import pandas as pd

df = pd.read_csv('property-data.csv')
print(df)
new_df = df.dropna()
print()
print(new_df.to_string())