import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

width, height = 10, 18

# Schriftgroesse
fsize = 12  # Allgemein

# Grundeinstellungen (Ticks nach innen, Schriftart)
tdir = 'in'
major = 5.0  # Länge major ticks
minor = 3.0  # Länge minor ticks
lwidth = 0.8  # Dicke Rahmen
lhandle = 2.0  # Länge handle in Legende

plt.style.use('default')
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'
plt.rcParams['font.size'] = fsize
plt.rcParams['xtick.major.size'] = major
plt.rcParams['xtick.minor.size'] = minor
plt.rcParams['ytick.major.size'] = major
plt.rcParams['ytick.minor.size'] = minor
plt.rcParams['axes.linewidth'] = lwidth
plt.rcParams['legend.handlelength'] = lhandle

time = [0, 0.4, 4, 8]

# read dc = 1e-5 gamma = 0.001 data
data1e5_001_0 = pd.read_csv('5e-5_0-001_0-1_data_t_0.csv')
data1e5_001_4 = pd.read_csv('5e-5_0-001_0-1_data_t_4.csv')
data1e5_001_40 = pd.read_csv('5e-5_0-001_0-1_data_t_40.csv')
data1e5_001_80 = pd.read_csv('5e-5_0-001_0-1_data_t_80.csv')

# read dc = 1e-5 gamma = 0.01 data
data1e5_01_0 = pd.read_csv('5e-5_0-001_1-0_data_t_0.csv')
data1e5_01_4 = pd.read_csv('5e-5_0-001_1-0_data_t_4.csv')
data1e5_01_40 = pd.read_csv('5e-5_0-001_1-0_data_t_40.csv')
data1e5_01_80 = pd.read_csv('5e-5_0-001_1-0_data_t_80.csv')

# read dc = 1e-1 gamma = 0.001 data
data1e1_001_0 = pd.read_csv('5e-5_0-01_0-1_data_t_0.csv')
data1e1_001_4 = pd.read_csv('5e-5_0-01_0-1_data_t_4.csv')
data1e1_001_40 = pd.read_csv('5e-5_0-01_0-1_data_t_40.csv')
data1e1_001_80 = pd.read_csv('5e-5_0-01_0-1_data_t_80.csv')

# read dc = 1e-1 gamma = 0.01 data
data1e1_01_0 = pd.read_csv('5e-5_0-01_1-0_data_t_0.csv')
data1e1_01_4 = pd.read_csv('5e-5_0-01_1-0_data_t_4.csv')
data1e1_01_40 = pd.read_csv('5e-5_0-01_1-0_data_t_40.csv')
data1e1_01_80 = pd.read_csv('5e-5_0-01_1-0_data_t_80.csv')

# get x data
x = list(data1e1_001_0['Points:1'] - 0.5)

# get plot over line data for dc = 1e-5 and gamma = 0.001 data
pol_1e5_001_c_0 = list(data1e5_001_0['c'])
pol_1e5_001_e_0 = list(data1e5_001_0['e'])
pol_1e5_001_m_0 = list(data1e5_001_0['m'])

pol_1e5_001_c_4 = list(data1e5_001_4['c'])
pol_1e5_001_e_4 = list(data1e5_001_4['e'])
pol_1e5_001_m_4 = list(data1e5_001_4['m'])

pol_1e5_001_c_40 = list(data1e5_001_40['c'])
pol_1e5_001_e_40 = list(data1e5_001_40['e'])
pol_1e5_001_m_40 = list(data1e5_001_40['m'])

pol_1e5_001_c_80 = list(data1e5_001_80['c'])
pol_1e5_001_e_80 = list(data1e5_001_80['e'])
pol_1e5_001_m_80 = list(data1e5_001_80['m'])

# get plot over line data for dc = 1e-5 and gamma = 0.01 data
pol_1e5_01_c_0 = list(data1e5_01_0['c'])
pol_1e5_01_e_0 = list(data1e5_01_0['e'])
pol_1e5_01_m_0 = list(data1e5_01_0['m'])

pol_1e5_01_c_4 = list(data1e5_01_4['c'])
pol_1e5_01_e_4 = list(data1e5_01_4['e'])
pol_1e5_01_m_4 = list(data1e5_01_4['m'])

pol_1e5_01_c_40 = list(data1e5_01_40['c'])
pol_1e5_01_e_40 = list(data1e5_01_40['e'])
pol_1e5_01_m_40 = list(data1e5_01_40['m'])

pol_1e5_01_c_80 = list(data1e5_01_80['c'])
pol_1e5_01_e_80 = list(data1e5_01_80['e'])
pol_1e5_01_m_80 = list(data1e5_01_80['m'])

# get plot over line data for dc = 1e-1 and gamma = 0.001 data
pol_1e1_001_c_0 = list(data1e1_001_0['c'])
pol_1e1_001_e_0 = list(data1e1_001_0['e'])
pol_1e1_001_m_0 = list(data1e1_001_0['m'])

pol_1e1_001_c_4 = list(data1e1_001_4['c'])
pol_1e1_001_e_4 = list(data1e1_001_4['e'])
pol_1e1_001_m_4 = list(data1e1_001_4['m'])

pol_1e1_001_c_40 = list(data1e1_001_40['c'])
pol_1e1_001_e_40 = list(data1e1_001_40['e'])
pol_1e1_001_m_40 = list(data1e1_001_40['m'])

pol_1e1_001_c_80 = list(data1e1_001_80['c'])
pol_1e1_001_e_80 = list(data1e1_001_80['e'])
pol_1e1_001_m_80 = list(data1e1_001_80['m'])

# get plot over line data for dc = 1e-1 and gamma = 0.01 data
pol_1e1_01_c_0 = list(data1e1_01_0['c'])
pol_1e1_01_e_0 = list(data1e1_01_0['e'])
pol_1e1_01_m_0 = list(data1e1_01_0['m'])

pol_1e1_01_c_4 = list(data1e1_01_4['c'])
pol_1e1_01_e_4 = list(data1e1_01_4['e'])
pol_1e1_01_m_4 = list(data1e1_01_4['m'])

pol_1e1_01_c_40 = list(data1e1_01_40['c'])
pol_1e1_01_e_40 = list(data1e1_01_40['e'])
pol_1e1_01_m_40 = list(data1e1_01_40['m'])

pol_1e1_01_c_80 = list(data1e1_01_80['c'])
pol_1e1_01_e_80 = list(data1e1_01_80['e'])
pol_1e1_01_m_80 = list(data1e1_01_80['m'])

# structure data to easily iterate over them
pol_1e5_001_c_data = [pol_1e5_001_c_0, pol_1e5_001_c_4, pol_1e5_001_c_40, pol_1e5_001_c_80]
pol_1e5_001_e_data = [pol_1e5_001_e_0, pol_1e5_001_e_4, pol_1e5_001_e_40, pol_1e5_001_e_80]
pol_1e5_001_m_data = [pol_1e5_001_m_0, pol_1e5_001_m_4, pol_1e5_001_m_40, pol_1e5_001_m_80]

pol_1e5_01_c_data = [pol_1e5_01_c_0, pol_1e5_01_c_4, pol_1e5_01_c_40, pol_1e5_01_c_80]
pol_1e5_01_e_data = [pol_1e5_01_e_0, pol_1e5_01_e_4, pol_1e5_01_e_40, pol_1e5_01_e_80]
pol_1e5_01_m_data = [pol_1e5_01_m_0, pol_1e5_01_m_4, pol_1e5_01_m_40, pol_1e5_01_m_80]

pol_1e1_001_c_data = [pol_1e1_001_c_0, pol_1e1_001_c_4, pol_1e1_001_c_40, pol_1e1_001_c_80]
pol_1e1_001_e_data = [pol_1e1_001_e_0, pol_1e1_001_e_4, pol_1e1_001_e_40, pol_1e1_001_e_80]
pol_1e1_001_m_data = [pol_1e1_001_m_0, pol_1e1_001_m_4, pol_1e1_001_m_40, pol_1e1_001_m_80]

pol_1e1_01_c_data = [pol_1e1_01_c_0, pol_1e1_01_c_4, pol_1e1_01_c_40, pol_1e1_01_c_80]
pol_1e1_01_e_data = [pol_1e1_01_e_0, pol_1e1_01_e_4, pol_1e1_01_e_40, pol_1e1_01_e_80]
pol_1e1_01_m_data = [pol_1e1_01_m_0, pol_1e1_01_m_4, pol_1e1_01_m_40, pol_1e1_01_m_80]

y = [1000 for i in range(len(x))]
    
# Create a figure with specified dimensions
fig, axs = plt.subplots(4, 2, figsize=(width, height))

for i, ax in enumerate(axs):
    axs[i, 0].plot(x, pol_1e5_001_e_data[i], color='cornflowerblue', linestyle='dotted')
    axs[i, 0].plot(x, pol_1e5_001_m_data[i], color='lightgreen', linestyle='dotted')
    axs[i, 0].plot(x, pol_1e5_001_c_data[i], color='orangered', linestyle='dotted')
    
    axs[i, 0].plot(x, pol_1e5_01_e_data[i], color='cornflowerblue', linestyle='solid')
    axs[i, 0].plot(x, pol_1e5_01_m_data[i], color='lightgreen', linestyle='solid')
    axs[i, 0].plot(x, pol_1e5_01_c_data[i], color='orangered', linestyle='solid')
    
    axs[i, 1].plot(x, pol_1e1_001_e_data[i], color='cornflowerblue', linestyle='dotted')
    axs[i, 1].plot(x, pol_1e1_001_m_data[i], color='lightgreen', linestyle='dotted')
    axs[i, 1].plot(x, pol_1e1_001_c_data[i], color='orangered', linestyle='dotted')
    
    axs[i, 1].plot(x, pol_1e1_01_e_data[i], color='cornflowerblue', linestyle='solid')
    axs[i, 1].plot(x, pol_1e1_01_m_data[i], color='lightgreen', linestyle='solid')
    axs[i, 1].plot(x, pol_1e1_01_c_data[i], color='orangered',linestyle='solid')
        
    axs[i,0].set_ylim(-0.05, 1.05)
    axs[i,0].set_title(r'$t = ' + str(time[i])+'$', loc='center')
    
    axs[i,1].set_ylim(-0.05, 1.05)
    axs[i,1].set_title(r'$t = ' + str(time[i])+'$', loc='center')
    
    if i == 0:
        axs[i,0].plot(x, y, label=r'$d_c=5 \cdot 10^{-5}$   $\gamma=0.001$   $\mu_1=0.1$', color='black', linestyle = 'dotted')
        axs[i,0].plot(x, y, label=r'$d_c=5 \cdot 10^{-5}$   $\gamma=0.001$   $\mu_1=1.0$', color='black', linestyle = 'solid')
        
        axs[i,1].plot(x, y, label=r'$d_c=5 \cdot 10^{-5}$   $\gamma=0.01$   $\mu_1=0.1$', color='black', linestyle = 'dotted')
        axs[i,1].plot(x, y, label=r'$d_c=5 \cdot 10^{-5}$   $\gamma=0.01$   $\mu_1=1.0$', color='black', linestyle = 'solid')
        
        axs[i,0].legend()
        axs[i,1].legend()
        
    if i == 3:
        axs[i, 1].plot(x, pol_1e1_01_e_data[i], color='cornflowerblue',label=r'$e$', linestyle='solid')
        axs[i, 1].plot(x, pol_1e1_01_m_data[i], color='lightgreen',label=r'$m$', linestyle='solid')
        axs[i, 1].plot(x, pol_1e1_01_c_data[i], color='orangered',label=r'$c$', linestyle='solid')
        axs[i,1].legend()

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()


