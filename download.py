import os
import requests

# NYC Taxi Parquet file URL
url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet'
filename = 'yellow_tripdata_2022-01.parquet'

# Download if not already present
if not os.path.exists(filename):
    print(f"Downloading {filename}...")
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print("Download complete.")
else:
    print("File already exists.")

