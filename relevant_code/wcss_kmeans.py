#import the K-Means algorithm from sklearn
from sklearn.cluster import KMeans 

#create a list for the wcss parameter
wcss = []

#test with 14 clusters
for i in range(1, 15):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 11)
    kmeans.fit(df_standardized)
    wcss.append(kmeans.inertia_)

wcss
