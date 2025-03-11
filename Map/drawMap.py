import folium
import openrouteservice

def drawMap(coord, output="map.html"):
    client = openrouteservice.Client(key='5b3ce3597851110001cf6248d8243e72d99c47a191d51dac7853e5e0')
    routes = client.directions(coordinates=coord, profile='driving-car', format='geojson')
    print(routes)

if __name__ == "__main__":
    coord = ((-122.4183, 37.7750), (-122.4187, 37.7753))
    drawMap(coord)