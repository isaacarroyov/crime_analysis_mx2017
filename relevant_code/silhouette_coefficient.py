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
print( 'Optimal number of cluters:', np.argmax(sil_values) + 2 )
