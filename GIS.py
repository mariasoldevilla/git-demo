# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 10:26:21 2018

@author: a911317
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import csv


#from mpl_toolkits.basemap import Basemap
# setting parameters for title and axes
font = {'family' : 'verdana',
        'size'   : 16}
matplotlib.rc('font', **font)

df = pd.DataFrame(pd.read_csv('C:/Users/a911317/OneDrive - Yara International ASA/TestGIS.csv',delimiter =','))
print df['S1'].describe()
# Grabbing the .csv data
lats,lons,S1 = [],[],[]
temp_dat = []

# How much to zoom from coordinates (in degrees)
zoom_scale = 3

# Setup the bounding box for the zoom and bounds of the map
bbox = [np.min(df['Latitude'])-zoom_scale,np.max(df['Latitude'])+zoom_scale,\
        np.min(df['Longitude'])-zoom_scale,np.max(df['Longitude'])+zoom_scale]

#fig, ax = plt.subplots(figsize=(12,7))
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# format colors for elevation range
S1_min = np.min(df['S1'])
S1_max = np.max(df['S1'])
cmap = plt.get_cmap('gist_earth')
normalize = matplotlib.colors.Normalize(vmin=S1_min, vmax=S1_max)



# plot elevations with different colors using the numpy interpolation mapping tool
# the range [50,200] can be changed to create different colors and ranges
for ii in range(0,len(S1)):
    color_interp = np.interp(S1[ii],[S1_min,S1_max],[0,100])
    plt.plot(df['Longitude'],df['Latitude'],marker='o',color=cmap(int(color_interp)))
    
    # format the colorbar 
cax, _ = matplotlib.colorbar.make_axes(ax)
cbar = matplotlib.colorbar.ColorbarBase(cax,norm=normalize,label='S1')

# save the figure and show it
#plt.savefig('asos_station_elevation.png', format='png', dpi=500,transparent=True)
plt.show()
