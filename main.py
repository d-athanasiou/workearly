import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


df=pd.read_csv('liquor.csv')

z_code='zip_code'
s_name='store_name'
i_num='item_number'
qty='bottles_sold'
pqs='perc_quant_stores'

# Calculate the sum of bottles sold in each store and transform the dataframe so that ypu can divide later
grouped = df.groupby(s_name)[qty].transform('sum')

# Divide the bottles sold of each item by the total bottle sold of the store, and multiply by 100 for percentage version
df[pqs] = df[qty] / grouped * 100

# Group the data by zip code , store name and item number, and calculate the sum of percentage for each item
g_sales = df.groupby([z_code, s_name , i_num])[[pqs, qty , z_code]].sum()

# Group the DataFrame by store and get the index of the row with the maximum quantity for each group
max_quantity_idx = g_sales.groupby(s_name)[pqs].idxmax()

# Select the rows with the maximum quantity for each store
max_quantity_items = g_sales.loc[max_quantity_idx]

# Using the quantity of bottles sold for each item that achieved the highest popularity in each store
# Plot x axis as zip code, y axis as bottles sold , each point created as described above

x = np.array(max_quantity_items[z_code])
y = np.array(max_quantity_items[qty])
colors = cm.jet(np.linspace(0, 1, len(x)))
plt.scatter(x, y, c=colors)
plt.xlabel('Zip Code')
plt.ylabel(' Bottles Sold ')
plt.title(' Bottles Sold ')
plt.show()

