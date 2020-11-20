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

#============ Elbow Method =====================================

#create a list for the wcss parameter
wcss = []

#test with 14 clusters
for i in range(1, 15):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 11)
    kmeans.fit(df_standardized)
    wcss.append(kmeans.inertia_)

#============= end Elbow Method =============================================

#========================= Silhouette method

from sklearn.metrics import silhouette_samples, silhouette_score

#create a list of K-Means models. Each element is a KMeans model with a specific number of clusters
kmeans2_sil= [KMeans(n_clusters=i, random_state=11, init='k-means++').fit(df_standardized) for i in range(1,15)]

#calculamos el silhouette score a cada modelo (de diferente número de clusters)
sil_values = [ silhouette_score(df_standardized, model.labels_, random_state=11)
                    for model in kmeans2_sil[1:]
                   ]
#save the silhouette coefficient in an array
sil_values = np.array( sil_values )
sil_values

print( 'Max. Silhouette Score:', sil_values[ np.argmax(sil_values) ] )
print( 'Optimal number of cluters:', np.argmax(sil_values) + 1 + 1 )

#============================ End Silhouette Method =======================

# ========================= Complementation plot

sns.set( style = 'white' )
plt.rc('font', family='serif')

fig , ax1 = plt.subplots( figsize = (10.5,6),
                         facecolor = c_background,
                         dpi = 200 )

ax1.set_title('Complementation: Elbow Method and Silhouette Method', size = 20, pad = 15 )
ax1.set_facecolor(c_background)

#--------------- WCSS -----------------
ax1.plot( range(2,15), wcss[1:],
         linestyle = '--', linewidth = 1.5,
         marker = 'P', markersize = 10,
         color = '#C83E4D' ,
         label = 'The Elbow Method'
        )
#----------- optimal number of clusters -----------------
ax1.plot( [5,5], [0,100],
         linestyle = ':', linewidth = 2,
         color = '#572F96' ,
        )

ax1.set_xlabel( 'Number of clusters', size = 15 )
ax1.set_ylabel('WCSS', size = 15 )
ax1.tick_params( axis = 'x', labelsize = 12 )
ax1.tick_params( axis = 'y', labelsize = 12, colors = '#C83E4D' )
ax1.yaxis.label.set_color( '#C83E4D' )
plt.legend(loc='upper center', prop = {'size':12})


# ------------- silhoutte coeff -------------
ax2 = ax1.twinx()
ax2.plot( range(2,15), sil_values,
         linestyle = ':', linewidth = 1.5,
         marker = 'o', markersize = 10,
         color = '#2F968B' ,
         label = 'The Silhouette Method'
        )

ax2.set_ylabel( '\nSilhoutte Coefficent', size = 15 )
ax2.tick_params( axis = 'y', labelsize = 12, colors = '#2F968B' )
ax2.yaxis.label.set_color( '#2F968B' )
plt.legend(loc=0, prop = {'size':12})


ax1.grid( b = True, linestyle = 'dashed', alpha = 0.5 )

plt.show()

#=========== the end of the plot ==========================
