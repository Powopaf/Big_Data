import folium
import requests
import openrouteservice

URL = "http://localhost:8082/ors/v2/directions/driving-car"
HEADERS: dict[str, str] = {"Content-Type": "application/json"}

def draw_trips_map(trips: any, output_file="trips_map.html") -> None:
    m: Map = folium.Map(location=[trips[0][0][1], trips[0][0][0]], zoom_start=13)
    
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
        [[-73.985619, 40.750554], [-73.977046, 40.758896]],
        [[-73.978889, 40.752778], [-73.980000, 40.730000]]
    ]
    draw_trips_map(trips)
