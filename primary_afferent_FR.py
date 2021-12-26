# primary afferent firing rates:
# plotting the firing rate functions for primary afferents

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

cm = 1/2.54  # allows you to plot in cm instead of inches
font = {'family' : 'Arial Narrow',
        'weight' : 'normal',
        'size'   : 8}

plt.rc('font', **font)

def rate_SAI():
    t = [ x for x in np.arange(0, 10001, 1) ]

    rate = []

    for i, key in enumerate(t):
        if i < len(t):
            freq_SAI = ( -1.45433609113392e-10 * key ** 3 + 1.340603396708e-6 * key ** 2 - 0.00378224210238498 * key + 4.52737468545426 ) * 8 
            rate.append(freq_SAI)

    return rate, t

def rate_SAII():
    t = [ x for x in np.arange(0, 10001, 1) ]

    rate = []

    for i, key in enumerate(t):
        if i < len(t):
            freq_SAII = ( -1.45433609113392e-10 * key ** 3 + 1.340603396708e-6 * key ** 2 - 0.00378224210238498 * key + 4.52737468545426 ) * 8 
            rate.append(freq_SAII)

    return rate, t

def rate_Ad():
    t = [ x for x in np.arange(0, 10001, 1) ]

    rate = []

    for i, key in enumerate(t):
        if i < len(t):
            freq_Ad = ( -7.265297e-15 * key ** 4 + 1.573831e-10 * key ** 3 - 8.201529e-7 * key ** 2 - 0.002539930 * key + 27.18412 ) 
            rate.append(freq_Ad)

    return rate, t

def rate_C():
    t = [ x for x in np.arange(0, 10001, 1) ]

    rate  = []

    for i, key in enumerate(t):
        if i < len(t):
            freq_C = (  9.630390e-15 * key ** 4 - 2.844577e-10 * key ** 3 + 3.012887e-6 * key ** 2 - 0.01400381 * key + 31.86546 )
            rate.append(freq_C)

    return rate, t

rate_C, t = rate_C()
rate_Ad, t2 = rate_Ad()
rate_Ab, t3 = rate_SAI()

real_Ab_spk = [ 5.7115, 3.8787, 3.6197, 3.1312, 2.8066, 2.6132, 2.4197, 2.259, 2.3934, 
            2.1672, 2.1049, 1.7475, 2.0131, 1.3606, 1.8229, 1.4983, 1.6983, 1.2754, 1.1147, 
            1.0, 1.0, 1.0, 1.0]
time_bin = 0.1
real_Ab =  [x / time_bin for x in real_Ab_spk] # num of spks / size of bin (0.1s) = rate in spk/s
x2 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 3000, 4000, 5000]

real_C =  [ 25.955, 15.755, 11.933,  9.573,  8.427 ]
real_C_std   = [ 2.231, 1.785, 1.382, 1.071, 1.174 ]
real_Ad= [ 25.538, 22.615, 17.385, 13.846, 10.769 ]
real_Ad_std  = [ 3.763, 3.395, 2.805, 2.696, 2.283 ]
x = [1000, 2000, 3000, 4000, 5000]

fig, ax = plt.subplots(3, sharex=True, figsize=(4*cm, 6*cm), dpi=1200)
ax[0].plot(t3,rate_Ab,color = 'k',linewidth = 1.0)
ax[0].errorbar(x2, real_Ab, fmt = 'o', capsize = 3,elinewidth=0.25, color = 'red', marker = 'o',markersize=2,linewidth = 0.5)
ax[0].set_ylim(0,50)
ax[0].set_xlim(0,5500)
ax[0].set_xticks([0,1000,2000,3000,4000,5000])
ax[0].set_yticks([0,25,50])

ax[1].plot(t2,rate_Ad,color = 'k',linewidth = 1)
ax[1].errorbar(x, real_Ad, fmt = 'o', elinewidth=0.5, capsize = 3, color = 'red', marker = 'o',markersize=2,linewidth = 0.5)
ax[1].set_ylim(0,50)
ax[1].set_xlim(0,5500)
ax[1].set_xticks([0,1000,2000,3000,4000,5000])
ax[1].set_yticks([0,25,50])
#ax[1].set_ylabel('Firing Rate (spk/s)')

ax[2].plot(t,rate_C, color = 'k',linewidth = 1)
ax[2].errorbar(x, real_C, fmt = 'o', elinewidth=0.5, capsize = 3, color = 'red', marker = 'o',markersize=2,linewidth = 0.5)
ax[2].set_ylim(0,50)
ax[2].set_xlim(0,5500)
ax[2].set_xticks([0,1000,2000,3000,4000,5000])
ax[2].set_yticks([0,25,50])
ax[2].set_xticklabels(labels=["0","1","2","3","4","5"])

for y in range(0,len(ax)):
    #plt.setp(ax[y].lines, color='k', linewidth=0.5)
    #plt.setp(ax[y].artists, edgecolor='k',linewidth=0.5)

    for axis in ['left','bottom']:
        ax[y].spines[axis].set_linewidth(0.5)
        ax[y].spines[axis].set_color('k')
  
    ax[y].spines['top'].set_visible(False)
    ax[y].spines['right'].set_visible(False)

#plt.xlabel('Time (s)')
#plt.ylabel('Firing Rate (spk/s)')
plt.tight_layout()

fig.savefig('FigureXA.svg', format='svg', dpi=1200)
fig.savefig('FigureXA.png', format='png', dpi=1200)



DataMatrix = pd.read_excel(r'/Users/lauramedlock 1/Desktop/Modeling-Projects/SDH-Model/Figures/Afferents/Average-FiringRates.xlsx')

pal = {"AB":"#986632","Ad":"#cb9932","C":"#666733","C2":"#989836"}
fig2, axs = plt.subplots(1, sharex=True, figsize=(6*cm, 6*cm), dpi=1200)
axs = sns.barplot(x="Force",y="Mean FR",hue="Fibre",palette=pal,data=DataMatrix,capsize=.1,linewidth=0.5)
axs = sns.stripplot(x="Force",y="Mean FR",data=DataMatrix,hue="Fibre", palette=pal, jitter=False, size=3,edgecolor="black",dodge=True,linewidth=0.5)
axs.set(xlabel='Mechanical Force (mN)', ylabel='Average Firing Rate (spk/s)')
axs.set_xticklabels(labels=["50","100","200"])
axs.set_ylim([0,18])
axs.set_yticks([0,2,4,6,8,10,12,14,16,18])
axs.legend_.remove()
axs.spines['top'].set_visible(False)
axs.spines['right'].set_visible(False)
plt.tight_layout()
plt.setp(axs.lines, color='k', linewidth=0.5)
plt.setp(axs.artists, edgecolor='k',linewidth=0.5)
for axis in ['left','bottom']:
  axs.spines[axis].set_linewidth(0.5)
  axs.spines[axis].set_color('k')

fig2.savefig('PrimaryAfferentFiring.svg', format='svg', dpi=1200)
fig2.savefig('PrimaryAfferentFiring.png', format='png', dpi=1200)