import pandas as pd
import time
import requests

# Load the CSV file using pandas
df = pd.read_csv('ip_addresses.csv')

# Sort the dataframe by the 'timestamp' column
df = df.sort_values('Timestamp')

# Initialize the previous timestamp with the first row's timestamp
prev_ts = None

server_url = 'http://server:5000'

# Iterate through each row in the dataframe
for index, row in df.iterrows():
    current_ts = float(row['Timestamp'])
    
    # On the first row, set the initial timestamp
    if prev_ts is None:
        prev_ts = current_ts

    # Calculate the delay (in seconds) between the current and previous package
    delay = current_ts - prev_ts
    if delay > 0:
        time.sleep(delay)

    # Convert the pandas Series row to a dictionary
    package = row.to_dict()

    # Send the package in JSON format using a GET request
    try:
        response = requests.get(f'{server_url}/traffic', json=package)
        print(f"Sent package: {package} - Response status: {response.status_code}")
    except Exception as e:
        print("Error sending package:", e)
    
    # Update the previous timestamp to current
    prev_ts = current_ts