import gmplot
import pandas as pd
import webbrowser

# This a private API key provided by Google Maps
apikey = 'AIzaSyD0aK745j_yg-ifDjtKsM8Zi5q2QSUuBlA'


# Function to draw the polygon of Medellin, reading all the coordinates from a csv file
# and returning the latitude and longitude of the coordinates
def draw_polygon():
    longitudes = []
    latitudes = []
    area = pd.read_csv('./data/poligono_de_medellin.csv', sep=';')
    polygon = str(area['geometry'].to_list()[0])[9:-2].split(',')
    for coordinates in polygon:
        long, lat = list(map(float, coordinates[1:].split(' ')))
        longitudes.append(long)
        latitudes.append(lat)
    return latitudes, longitudes


# Function to assign the coordinates of the path to the latitude and longitude lists
def assign_coordinates(path):
    lat = []
    long = []
    for coord in path:
        lat, long = zip(*path)
    return lat, long


# Function to draw the map of Medellin with the polygon and the path
# With different functions of the gmplot library
# We can create markers, polylines and polygons that will be added to the map
def draw_map(path):
    limit_latitude, limit_longitude = draw_polygon()
    lat, long = assign_coordinates(path)

    gmp_draw = gmplot.GoogleMapPlotter(6.267203842477565, -75.579710387, 10, apikey=apikey)
    gmp_draw.polygon(limit_latitude, limit_longitude, face_color='white', face_alpha=0.4, edge_color='grey',
                     edge_width=5)
    gmp_draw.scatter(lat, long, 'green', size=3, marker=False)
    gmp_draw.plot(lat, long, 'green', edge_width=4)
    gmp_draw.marker(lat[0], long[0], label='A', color='blue')
    gmp_draw.marker(lat[-1], long[-1], label='B', color='red')

    gmp_draw.draw('map.html')
    webbrowser.open_new_tab('map.html')
