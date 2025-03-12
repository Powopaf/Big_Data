import folium
import requests
import openrouteservice

URL = "http://localhost:8082/ors/v2/directions/driving-car"
HEADERS: dict[str, str] = {"Content-Type": "application/json"}

def draw_trips_map(trips, output_file="trips_map.html"):
    m = folium.Map(location=[trips[0][0][1], trips[0][0][0]], zoom_start=13)
    
    for i, coordinates in enumerate(trips):
        
        data = {
            "coordinates": coordinates,
            "instructions": False
        }
        response = requests.post(URL, json=data, headers=HEADERS)
        
        route = response.json()
        
        polyline = route["routes"][0]["geometry"]
        route_coords = openrouteservice.convert.decode_polyline(polyline)["coordinates"]
        
        route_coords = [[lat, lon] for lon, lat in route_coords]
        
        folium.PolyLine(route_coords, color="red", weight=3, opacity=0.7).add_to(m)
    
    m.save(output_file)
    print(f"Map saved as {output_file}")

if __name__ == "__main__":
    
    trips = [
        [[-73.991957, 40.721567], [-73.993803, 40.695922]],
        [[-73.982102, 40.73629], [-73.95585, 40.76803]],
        [[-74.002587, 40.739748], [-73.869983, 40.770225]],
        [[-73.974267, 40.790955], [-73.996558, 40.731849]],
        [[-74.00158, 40.719382], [-73.996558, 40.731849]]
    ]
    draw_trips_map(trips)
