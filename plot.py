import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
# set height of bar
# data = pd.DataFrame({
#  'year' : [1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020],
#  'inflatiuon_factor' : [4.96,4.69,4.41,4.1,3.68,3.24,2.94,2.77,2.68,2.57,2.48,2.44,2.35,2.26,2.15,2.04,1.96,1.9,1.85,1.8,1.75,1.7,1.66,1.64,1.6,1.55,1.51,1.48,1.45,1.41,1.37,1.32,1.3,1.2,1.2,1.2,1.2,1.2,1.2,1.1,1.1,1.1,1.1,1.1,1.0,1.0],
#  'wind_budget' : [57.3,14.4,22.3,36.7,59.3,60.2,54.1,34.1,31.4,26.4,28.4,27.3,8.4,16.8,8.8,9.9,11.4,21.4,24.3,30.3,48.8,32.7,29.3,33.2,33.2,32.7,38.2,37.3,42.3,41.2,40.2,38.2,49.0,49.0,54.4,79.0,78.8,91.8,86.1,87.0,105.9,95.5,90.0,92.0,92.0,104.0],
#  'water_budget' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 9.4, 30, 35.6, 22.2, 34, 31.6, 41.3, 41.1, 44.25, 59, 70, 70, 109],
#  'wind_generation' : [0,0,0,0,0,0,0,0,0,0.01,0.01,0,0,0,2.11,2.79,2.95,2.89,3.01,3.45,3.16,3.23,3.29,3.03,4.49,5.59,6.74,10.35,11.19,14.14,17.81,26.59,34.45,55.36,73.89,94.65,120.18,140.82,167.84,181.66,190.72,226.99,254.3,272.67,294.91,337.51]})
file_path = "capacity_data.csv"  # R
data = pd.read_csv(file_path)


barWidth = 0.33
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
 
# Make the plot
ax1.bar(data.year-barWidth, data.wind_budget*data.inflation_factor, width = barWidth, label ='Wind Program Budget')
ax1.bar(data.year+barWidth, data.water_budget*data.inflation_factor, width = barWidth,label ='Marine Energy Program Budget')
ax2.plot(data.year, data.wind_generation,color='k',linewidth=2,label='Wind electricity generation')
ax2.grid(False)
ax1.grid(False)
 
# Adding Xticks
ax1.set_xlabel('Year', fontweight ='bold', fontsize = 10)
ax1.set_ylabel('Inflation adjusted budget ($M)', fontweight ='bold', fontsize = 12)
ax2.set_ylabel('Wind electricity generation (TWh/year)', fontweight ='bold', fontsize = 12)
ax2.set_ylim([0,350])
ax1.set_xlim([1975,2022])
ax2.set_xlim([1975,2022])
# ax1.axes.set_xticklabels([r + barWidth for r in range(len(data.wind_budget_inflation))],
#         data.plot_keys)
# ax1.axes.set_xticklabels()
 
ax1.legend()
ax2.legend()

barWidth = 0.33
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
 
# Make the plot
ax1.bar(data.year-barWidth, data.wind_budget*data.inflation_factor, width = barWidth, label ='Wind Program Budget')
ax1.bar(data.year+barWidth, data.water_budget*data.inflation_factor, width = barWidth,label ='Marine Energy Program Budget')
ax2.plot(data.year, data.wind_generation,color='k',linewidth=2,label='Wind electricity generation')
ax2.grid(False)
ax1.grid(False)
 
# Adding Xticks
ax1.set_xlabel('Year', fontweight ='bold', fontsize = 10)
ax1.set_ylabel('Inflation adjusted budget ($M)', fontweight ='bold', fontsize = 12)
ax2.set_ylabel('Wind electricity generation (TWh/year)', fontweight ='bold', fontsize = 12)
ax2.set_ylim([0,350])
ax1.set_xlim([1975,2022])
ax2.set_xlim([1975,2022])
# ax1.axes.set_xticklabels([r + barWidth for r in range(len(data.wind_budget_inflation))],
#         data.plot_keys)
# ax1.axes.set_xticklabels()
 
ax1.legend()
ax2.legend()

plt.show()