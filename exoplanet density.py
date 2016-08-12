'''
Exoplanets
'''

from __future__ import division
import numpy as np
import pandas as pd
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math

userpath='/Users/Nicole/Desktop/'
filename='exoplanet_catalog.csv'
os.chdir(userpath)
data=pd.read_csv(filename)             #path to exoplanet excel doc


density=1000 #density of water in kg/m**3
d=.1
data = data[(data.mass_error_min/data.mass)<=d]
data = data[(data.mass_error_max/data.mass)<=d]
data = data[(data.radius_error_min/data.radius)<=d]
data = data[(data.radius_error_max/data.radius)<=d]

 
#data = data[(data.mass_error_min/data.mass)<=c and (data.mass_error_max/data.mass)<=c and (data.radius_error_min/data.mass)<=c and (data.radius_error_max/data.mass)<=c]

#m=[]                          #data without 10%

#mass=data.mass                
#min_error=data.mass_error_min
#max_error=data.mass_error_max #min and max mass
#
#r=[]                          #empty array
#radius=data.radius
#minr=data.radius_error_min
#maxr=data.radius_error_max    #min and max radius



#for val in mass:
  #  pe_mass_min=min_error[val]/mass[val]
   # pe_mass_max=max_error[val]/mass[val]
    #pe_radius_min=min_error[val]/radius[val]
    #pe_radius_max=max_error[val]/radius[val]
    #if pe_mass_min<=c and pe_mass_max<=c and pe_radius_min<=c and pe_radius_max<=c: m.append(mass[val])



#array_of_mass=np.arange(0, 100, 1)   #array of mass converted to Kg
#array_of_radius=pow((array_of_mass)/(density*(4/3)*np.pi), 1/3) #array of radius converted to m

plt.figure(11)                          #plot graph
plt.scatter(data.mass, data.radius) 
t=np.arange(100)
x=((3*data.mass)/(4*math.pi*data.radius**3))
#array=(0,100,1)
o=[]
for i in range(1,100+1):
    o.append(i)
plt.scatter(data.mass, data.radius, c=x)

plt.xlim(0,70)
plt.ylim(0,2.5)
plt.yscale('linear')
plt.xscale('linear')
plt.colorbar()
clb.set_label('Density (Mjup/Vjup)')
plt.xlabel ('Mass (Mj)')
plt.ylabel ('Radius (Rj)')
plt.title ('Relationships Between the Mass and Radius of Exoplanets')
#plt.plot(array_of_mass, array_of_radius)

plt.savefig('exoplanet4.png')