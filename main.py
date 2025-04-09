from pyhive import hive

# Connect to Hive
conn = hive.Connection(host='localhost', port=10000, username='hive')
cursor = conn.cursor()

# Execute a query
cursor.execute('SELECT * FROM my_table LIMIT 10')

# Get column names
columns = [desc[0] for desc in cursor.description]
print("Column names:", columns)

# Print rows
for row in cursor.fetchall():
    print(row)

