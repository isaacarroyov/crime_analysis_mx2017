#colours of each bar chart
colores_barchart6 = ['#0B3954', '#43AA8B', '#DF5957', '#FFCA3A', '#7D3274', '#4C83BF']

#titles 
titulos = ['Crimes by State. \nType: Homicides',
           'Crimes by State. \nType: Car theft', 'Crimes by State. \nType: Extortion',
           'Crimes by State. \nType: Theft/Assault on the street or public transportation', 
           'Crimes by State. \nType: Home theft', 'Crimes by State. \nType: Fraud',
          ]

#create a data frame without the 'POBLACION' and 'PP_URBANA' columns
df_barchart6 = df.drop( ['POPULATION','URBAN_PP'], axis = 'columns' )

#dropped 'POBLACION' and 'PP_URBANA' in order to have the crime variables
variables_barchart6 = df_barchart6.columns.values[3:]

#---------------------- PLOTTING THE BAR CHARTS ----------------------------------------------

#create a figure
plt.figure( figsize=(27,3),
           dpi = 100,
           facecolor=c_background
          )
plt.axes().set_facecolor( c_background )

#using a for loop we plot every subplot of information
for i in range(len(titulos)):

    #sort values in descending order for each type of crime 
    df_barchart6 = df_barchart6.sort_values( by = variables_barchart6[i], ascending = False )

    #create a subplot
    plt.subplot( 3, 2, i+1 )

    #make the bar chart
    plt.bar( df_barchart6['ID'], df_barchart6[ variables_barchart6[i] ],
            color = colores_barchart6[i] #choose a colour from the list
           )
    
    #add title and labels on the axes
    plt.title( titulos[i], size = 25, pad = 15 )
    plt.xlabel( 'State [ ID ]', size = 20 )
    plt.ylabel( 'Number of registered cases \n (per 100 thousand inhabitants)', size = 20 )
    plt.xticks( rotation = 90 )
    plt.tick_params( labelsize = 17 )

#adjust subplots
plt.subplots_adjust( top = 7, bottom= 0.01, 
                    hspace=0.4 )
plt.show()
