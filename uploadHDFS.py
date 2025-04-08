from hdfs import InsecureClient

# HDFS client configuration
hdfs_url = 'http://namenode:50070'
client = InsecureClient(hdfs_url, user='hadoop')

# Local file path
local_file = './DataBase/yellow_tripdata_2022-01.parquet'
hdfs_path = '/user/hadoop/yellow_tripdata_2022-01.parquet'

# Upload file to HDFS
client.upload(hdfs_path, local_file)
print(f'File {local_file} uploaded to HDFS at {hdfs_path}')

