import folium
import requests
import openrouteservice  # Add this line for decoding the polyline

# ORS API endpoint
url = "http://localhost:8082/ors/v2/directions/driving-car"

# Define start and end coordinates
coordinates = [[-73.991957, 40.721567], [-73.993803, 40.695922]]

# Request payload
data = {
    "coordinates": coordinates,
    "instructions": False
}

# Make the API request
headers = {"Content-Type": "application/json"}
response = requests.post(url, json=data, headers=headers)

# Check if the request was successful
if response.status_code != 200:
    print(f"Error: {response.status_code}, Response: {response.text}")
    exit()

# Parse response
route = response.json()

# Extract and decode route geometry
try:
    polyline = route["routes"][0]["geometry"]  # This is a compressed polyline string
    route_coords = openrouteservice.convert.decode_polyline(polyline)["coordinates"]
except (KeyError, IndexError, TypeError) as e:
    print("Error extracting route coordinates:", e)
    print("Response structure:", route)
    exit()

# Convert coordinates to folium format ([latitude, longitude])
route_coords = [[lat, lon] for lon, lat in route_coords]

# Create the folium map
m = folium.Map(location=route_coords[0], zoom_start=14)

# Add route as a polyline
folium.PolyLine(route_coords, color="blue", weight=5, opacity=0.7).add_to(m)

# Add markers for start and end points
folium.Marker(route_coords[0], popup="Start", icon=folium.Icon(color="green")).add_to(m)
folium.Marker(route_coords[-1], popup="End", icon=folium.Icon(color="red")).add_to(m)

# Save map
m.save("trip_map.html")
print("Map saved as trip_map.html")
