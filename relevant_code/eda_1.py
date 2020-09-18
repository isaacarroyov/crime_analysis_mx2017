#number of columns and rows 
df.shape

#name of the columns
df.columns.values

#type of data we have
df.dtypes

#relevant stats ordered in descending order (mean)
df.describe().transpose().iloc[1:-2].sort_values(by = 'mean', ascending = False)

# - - - - - - - - - - - - - - DATA DISTRIBUTION - - - - - - - - - - - - - - - - 

#seaborn font size and style of plot
sns.set( font_scale = 1.5, style = 'white' )

#matplotlib font type
plt.rc('font', family='serif')

df.iloc[:,3:].hist( figsize=(18,15), bins=15,
                   xlabelsize = 15, ylabelsize = 15,
                   color = '#72BFA8',
                   grid = False)
