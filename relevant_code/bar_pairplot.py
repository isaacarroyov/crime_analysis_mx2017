"""
I this Python file you're going to find the code to plot the
bar chart and the pairplot shown in the Medium's article

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

#====== Making the bar chart ==========================
#colours of each bar chart
colours_barchart6 = ['#0B3954', '#43AA8B', '#DF5957', '#FFCA3A', '#7D3274', '#4C83BF']

#titles
titles = ['Crimes by State. \nType: Homicides',
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
for i in range(len(titles)):

    #sort values in descending order for each type of crime
    df_barchart6 = df_barchart6.sort_values( by = variables_barchart6[i], ascending = False )

    #create a subplot
    plt.subplot( 3, 2, i+1 )

    #make the bar chart
    plt.bar( df_barchart6['ID'], df_barchart6[ variables_barchart6[i] ],
            color = colours_barchart6[i] #choose a colour from the list
           )

    #add title and labels on the axes
    plt.title( titles[i], size = 25, pad = 15 )
    plt.xlabel( 'State [ ID ]', size = 20 )
    plt.ylabel( 'Number of registered cases \n (per 100 thousand inhabitants)', size = 20 )
    plt.xticks( rotation = 90 )
    plt.tick_params( labelsize = 17 )

#adjust subplots
plt.subplots_adjust( top = 7, bottom= 0.01,
                    hspace=0.4 )
plt.show()
#======= Making the pairplot ============================

variables = np.array( [ 'HOMICIDES', 'CAR_THEFT', 'EXTORTION', 'STREET_TRANSPORT_THEFT' ] )

#relative size of the labels on the pairplot
sns.set( font_scale = 1.3, style = 'white' )
plt.rc('font', family='serif')

sns.pairplot( df[ variables ],
             kind = 'reg',
             height= 3.0, aspect=1.0,
            )
plt.show()
