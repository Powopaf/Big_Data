import os
import requests

# Create the DataBase directory if it doesn't exist
data_dir = './DataBase'
os.makedirs(data_dir, exist_ok=True)

# NYC Taxi Parquet file URL
url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet'
filename = 'yellow_tripdata_2022-01.parquet'

# Full path to save the file
file_path = os.path.join(data_dir, filename)

# Download if not already present
if not os.path.exists(file_path):
    print(f"Downloading {filename} to {file_path}...")
    response = requests.get(url)
    with open(file_path, 'wb') as f:
        f.write(response.content)
    print("Download complete.")
else:
    print(f"File already exists at {file_path}.")

