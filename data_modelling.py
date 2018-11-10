# IMPORTS HERE
import pandas as pd;
import matplotlib.pyplot as plt;

df = pd.read_csv('C:\Users\sharm\OneDrive\Desktop\documentClassification\_csv_data\data.csv', names=['doctype', 'details'])

_head_n = df.head(5)
_tail_n = df.tail(5)
_df_shape = df.shape
_df_info = df.info()

det =  df['details'].isnull()


fig = plt.figure(figsize=(8,6))
df.groupby('doctype').details.count().plot.bar(ylim=0)
plt.show()

#print _tail_n;
#print _df_shape #Tell you about the number of rows and columns (rows,cols)
#print pd.isnull()
