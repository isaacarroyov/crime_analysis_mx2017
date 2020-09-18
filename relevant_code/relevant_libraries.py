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

df = pd.read_csv('/data/CrimesMX2017.csv', encoding='ISO-8859-1')
