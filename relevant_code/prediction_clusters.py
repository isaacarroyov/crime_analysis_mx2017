#Use of n_clusters = 5
kmeans = KMeans( n_clusters=5, init='k-means++', random_state=11 )

#train and prediction on our normalized data
predicted_y = kmeans.fit_predict( df_standardized )

#numbers of cluster goes from 0 to 4, we're adding +1 to the array
predicted_y = predicted_y + 1 

df['CLUSTER'] = predicted_y
