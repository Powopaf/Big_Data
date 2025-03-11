import folium
import requests

# ORS API endpoint (make sure ORS is running locally)
# url = "http://localhost:8082/ors/v2/directions/driving-car"
url = "http://localhost:8082/ors/v2/directions/driving-car"
# Define start and end coordinates (longitude, latitude format)
coordinates = [[-73.991957, 40.721567], [-73.993803, 40.695922]]

# Request payload
data = {
    "coordinates": coordinates,
    "profile": "driving-car",
    "instructions": False  # Set to True if you want step-by-step directions
}

# Make the API request
headers = {"Content-Type": "application/json"}
response = requests.post(url, json=data, headers=headers)
route = response.json()
print(route)
# Extract route geometry (list of [longitude, latitude] points)
# route_coords = route["routes"][0]["geometry"]["coordinates"]

# Convert coordinates to folium format ([latitude, longitude])
# route_coords = [[lat, lon] for lon, lat in route_coords]

# Create the folium map centered at the start location
# m = folium.Map(location=route_coords[0], zoom_start=14)

# Add route as a polyline
# folium.PolyLine(route_coords, color="blue", weight=5, opacity=0.7).add_to(m)

# Add markers for start and end points
# folium.Marker(route_coords[0], popup="Start", icon=folium.Icon(color="green")).add_to(m)
# folium.Marker(route_coords[-1], popup="End", icon=folium.Icon(color="red")).add_to(m)

# Save map as an HTML file
# m.save("trip_map.html")
print("Map saved as trip_map.html")

