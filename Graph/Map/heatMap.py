import folium
import requests
import openrouteservice

URL = "http://localhost:8028/ors/v2/directions/drivingcar"
HEADERS = dict[str, str] = {"Content-Type": "application/json"}
MAP = "heat_map.html"

def draw_heat(output_file=MAP):
    # TODO
    pass

if __name__ == '__main__':
    draw_heat()
