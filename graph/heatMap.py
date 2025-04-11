# may it work  ¯\_(ツ)_/¯

import folium
from folium.plugins import HeatMap

NYC = [40.7128, -74.0060]
MAP = "HeatMap.html"

def draw_heat(coordinates, output_file=MAP):
    m = folium.Map(location=NYC, zoom_start=13)
    HeatMap(coordinates, radius=12, blur=8, min_opacity=0.3).add_to(m)
    m.save(output_file)
    print(f"HeatMap save as {output_file}")
"""
if __name__ == '__main__':
    c = [[-73.991957, 40.721567], [-73.982102, 40.73629],
         [-74.002587, 40.739748], [-73.974267, 40.790955],
         [-74.00158, 40.719382]]
    draw_heat(c)
"""
