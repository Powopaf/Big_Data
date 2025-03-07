import folium

def createMap(coords, output="mapNYC.html") -> None:
    nyc_map: any = folium.Map(location=(40.7128, -74.0060), zoom_start=12)
    for lat, lon in coords:
        folium.CircleMarker(location=(lat, lon), radius=1, color="red", fill=True, fill_color="red").add_to(nyc_map)
    nyc_map.save(output)

if __name__ == '__main__':
    createMap([(40.721567,-73.991957), (40.695922, -73.993803)])