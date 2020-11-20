"""
I this Python file you're going to find the code for
'Data preprocessing: Standardization'

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

print(df_standardized)
