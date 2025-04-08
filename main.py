import pandas as pd

# Path to your Parquet file
file_path = "yellow_tripdata_2009-01.parquet"

# Load the Parquet file
df = pd.read_parquet(file_path)

# Print only the column names
for col in df.columns:
    print(col)

