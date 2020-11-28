import folium
import geojson
from folium.plugins import MarkerCluster

ozon = [[43.101010, 131.948338],
        [43.112434, 131.878115],
        [43.117154, 131.882482],
        [43.123695, 131.886836],
        [43.128426, 131.892511],
        [43.133207, 131.902996],
        [43.169214, 131.925219],
        [43.186311, 131.928825]
        ]


map = folium.Map(location=[43.164242, 131.905624], zoom_start=12)
marker_cluster = MarkerCluster().add_to(map)
with open("POI.geojson", encoding='UTF-8') as read_file:
    data = geojson.load(read_file)
    for i in range(2251):
        pos = data[i].get('geometry').get('coordinates')
        name = data[i].get('properties').get('name')
        pos[0], pos[1] = pos[1], pos[0]
        folium.CircleMarker(location=pos, popup=name, radius=9, color="red").add_to(marker_cluster)

num = 0
marker_cluster_buildings = MarkerCluster().add_to(map)
with open("buildings.geojson", encoding='UTF-8') as read_file:
    data = geojson.load(read_file)
    # позже разобратся почему не итерирует дата
    for i in range(60902):
        if data[i].get('properties').get('population') != None:
            geo = len(data[i].get('geometry').get('coordinates')[0][0])
            print(geo)
            population = data[i].get('properties').get('population')//geo
            print(population)
            for pos in data[i].get('geometry').get('coordinates')[0][0]:
                pos[0], pos[1] = pos[1], pos[0]
                num += 1
                print(num)
                folium.CircleMarker(location=pos, popup=population, radius=9, color="green").add_to(marker_cluster_buildings)
print('save map')
map.save("map1.html")