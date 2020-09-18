#create a figure to plot
plt.figure( dpi = 150,
           figsize=(7,5)
          )

#create a correlation matrix
corrMatrix = df[variables].corr().round(3)

#relative size of the labels on the heatmap
sns.set( font_scale= 0.8 )
plt.rc('font', family='serif')


#plot the heat map
sns.heatmap( corrMatrix, annot = True , cmap = 'BrBG', center=0 )

#rotate the x and y tiks
plt.xticks( rotation = 90 )
plt.yticks( rotation = 0 )
