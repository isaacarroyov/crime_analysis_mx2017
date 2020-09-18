#Here we standardize a dataset along any axis. Center to the mean and component wise scale to unit variance.
from sklearn import preprocessing
df_standardized = preprocessing.scale( df[variables] )
df_standardized = pd.DataFrame( df_standardized )
