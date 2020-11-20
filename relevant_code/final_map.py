"""
I this Python file you're going to find the code that leads
to the complementation plot of the silhouette method and the
elbow method.

This code was made by: Isaac Arroyo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#GENERAL PLOT SETTINGS

#style sheet
plt.style.use('seaborn-paper')

#background in plots
c_background = '#FFFFFF'

#color for the XYZ planes for the 3d plots
rgba_planes = (231/255, 231/255, 231/255)

#import the csv as a Data Frame
df = pd.read_csv('data/CrimesMX2017.csv', encoding='ISO-8859-1')

#select the relevant variables
variables = np.array( [ 'HOMICIDES', 'CAR_THEFT', 'EXTORTION', 'STREET_TRANSPORT_THEFT' ] )

#Here we standardize a dataset along any axis. Center to the mean and component wise scale to unit variance.
from sklearn import preprocessing
df_standardized = preprocessing.scale( df[variables] )
df_standardized = pd.DataFrame( df_standardized )

#import the K-Means algorithm from sklearn
from sklearn.cluster import KMeans

#knowing that the optimal number of clusters is 5

#Use of n_clusters = 5
kmeans = KMeans( n_clusters=5, init='k-means++', random_state=11 )

#train and prediction on our normalized data
predicted_y = kmeans.fit_predict( df_standardized )

#numbers of cluster goes from 0 to 4, we're adding +1 to the array
predicted_y = predicted_y + 1

#adding a column named CLUSTER
df['CLUSTER'] = predicted_y

# ===============  Making the map with folium ==============
df_dict = df.set_index( 'ID' )['CLUSTER']

states_geo = 'data/states_mx.json'

#use folium to create map
import folium
map_mex = folium.Map( location = [24,-102], zoom_start = 4.5 )

#colour a state according to its cluster
def my_color_function(feature):
    if df_dict[feature['id']] == 1:
        return colours_cluster[0]
    elif df_dict[feature['id']] == 2:
        return colours_cluster[1]
    elif df_dict[feature['id']] == 3:
        return colours_cluster[2]
    elif df_dict[feature['id']] == 4:
        return colours_cluster[3]
    elif df_dict[feature['id']] == 5:
        return colours_cluster[4]

for i in range(4):
    folium.GeoJson(
        states_geo,
        style_function=lambda feature: {
            'fillColor': my_color_function(feature),
            'color' : 'black',
            'fill_opacity' : 10.1,
            'weight' : 0.3,
            }
        ).add_to(map_mex)

# Generate and save the mapa_mex
map_mex.save('map_mex.html')


#final
