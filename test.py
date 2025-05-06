import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.ion()
plt.close('all')
 
# set height of bar
file_path = "capacity_data.csv"  # R
data = pd.read_csv(file_path)

# Create a NumPy vector of the same length as the data
data_length = np.arange(len(data))

barWidth = 0.4

fig1, ax1 = plt.subplots(1, 1,
                         num=101,
                         gridspec_kw=dict(left=0.1, right=0.9, bottom=0.1, top=0.9),
                         figsize=[9, 7]
                         )
ax2 = ax1.twinx()
 
# Make the plot
ax1.bar(data.year + barWidth / 2, data.wind_budget*data.inflation_factor, width = barWidth, label ='Wind Program Budget', color='tab:orange')
ax1.bar(data.year - barWidth / 2, data.water_budget*data.inflation_factor, width = barWidth,label ='Marine Energy Program Budget', color='blue')
ax2.plot(data.year, data.wind_generation,color='k',linewidth=2, label='Wind electricity generation', )
# ax2.plot(data.year, data.wind_installed_capacity,color='r',linewidth=2, label='Wind installed capacity', )
#ax2.plot(np.NaN, np.Nan, 'k-', linewidth=2, label='Wind electricity generation')
ax2.grid(False)
ax1.grid(False)
 
# Adding Xticks
ax1.set_xlabel('Year', fontsize = 16)
ax1.set_ylabel('Inflation adjusted budget ($M)', fontsize = 16)
ax2.set_ylabel('Wind electricity generation (TWh/year)', fontsize = 16)
ax2.set_ylim([0,500])
# ax1.axes.set_xticklabels([r + barWidth for r in range(len(data.wind_budget_inflation))],
#         data.plot_keys)
# ax1.axes.set_xticklabels()
 
ax1.legend(loc='upper left',
           bbox_to_anchor=[0.03, 0.98],
           prop=dict(size='large'),
           )

ax2.legend(loc='upper right',
           bbox_to_anchor=[0.98, 0.98],
           prop=dict(size='large'),
           )
ax1.tick_params(axis='both', which='major', labelsize=14)
ax2.tick_params(axis='both', which='major', labelsize=14)
ax1.set_xlim([1974.5, 2025.5])

#########################
fig2, ax3 = plt.subplots(1, 1,
                         num=102,
                         gridspec_kw=dict(left=0.1, right=0.9, bottom=0.1, top=0.9),
                         figsize=[9, 7]
                         )
ax4 = ax3.twinx()
 
 
# Make the plot
ax3.bar(data_length + barWidth / 2, data.wind_budget*data.inflation_factor, width = barWidth, label ='Wind Program Budget', color='tab:orange')
ax3.bar(data_length[33:]-33 - barWidth / 2, data.water_budget[33:]*data.inflation_factor[33:], width = barWidth, label='Marine Energy Program Budget', color='blue')
# ax4.plot(data_length, data.wind_generation,color='k',linewidth=2, label='Wind electricity generation', )
# ax4.plot(data_length, data.wind_installed_capacity, 'rs-', linewidth=2, label='Wind installed capacity')
#ax4.plot(np.NaN, np.Nan, 'k-', linewidth=2, label='Wind electricity generation')
ax4.grid(False)
ax3.grid(False)
 
# Adding Xticks
ax3.set_xlabel('Year', fontsize = 16)
ax3.set_ylabel('Inflation adjusted budget ($M)', fontsize = 16)
ax4.set_ylabel('Wind electricity generation (TWh/year)', fontsize = 16)
# ax4.set_ylim([0, 155000])  # Set y-axis limits for ax4 on a linear scale
ax4.set_yscale('linear')
# ax4.set_ylim([0,500])
# ax3.axes.set_xticklabels([r + barWidth for r in range(len(data.wind_budget_inflation))],
#         data.plot_keys)
# ax3.axes.set_xticklabels()
 
ax3.legend(loc='upper left',
           bbox_to_anchor=[0.03, 0.98],
           prop=dict(size='large'),
           )

ax4.legend(loc='upper right',
           bbox_to_anchor=[0.98, 0.98],
           prop=dict(size='large'),
           )
ax3.tick_params(axis='both', which='major', labelsize=14)
ax4.tick_params(axis='both', which='major', labelsize=14)
ax3.set_xlim([-.05, 50])

plt.figure()
plt.plot(data.year, data.wind_installed_capacity, 'ro-', label='Wind Installed Capacity')
plt.xlabel('Index', fontsize=14)
plt.ylabel('Wind Installed Capacity', fontsize=14)
plt.title('Wind Installed Capacity', fontsize=16)
plt.legend()
plt.grid(True)


plt.show()
input("Press Enter to close the plot...")

print(data.wind_installed_capacity)
# fig2.savefig('Marine-Wind_Program_Budgets.png', dpi=200)
# fig2.savefig('Marine-Wind_Program_Budgets.pdf')