import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point
# load shapefile



def print_map():
    df_points = pd.read_csv('output/airports.csv')
    geometry = [Point(xy) for xy in zip(df_points.longitude, df_points.latitude)]

    gdf_map = gpd.read_file('input/countries.geojson')
    gdf_points = gpd.GeoDataFrame(df_points, geometry=geometry)

    fig, ax = plt.subplots(figsize=(10, 10))

    gdf_map.plot(ax=ax, alpha=0.4, edgecolor='black')
    gdf_points.plot(ax=ax, color='red', markersize=10)
    plt.show()