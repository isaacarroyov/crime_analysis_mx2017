variables = np.array( [ 'HOMICIDES', 'CAR_THEFT', 'EXTORTION', 'STREET_TRANSPORT_THEFT' ] )

#relative size of the labels on the pairplot
sns.set( font_scale = 1.3, style = 'white' )
plt.rc('font', family='serif')

sns.pairplot( df[ variables ],
             kind = 'reg',
             height= 3.0, aspect=1.0,
            )
