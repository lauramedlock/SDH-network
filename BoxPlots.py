#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 09:51:05 2021
@author: lauramed
For plotting figures (Medlock et al. 2022)
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


font = {'family' : 'Arial Narrow',
        'weight' : 'normal',
        'size'   : 8}
plt.rc('font', **font)
cm = 1/2.54  # allows you to plot in cm instead of inches

# Box spacing for bxplot:
import numpy as np
from matplotlib.patches import PathPatch

def adjust_box_widths(g, fac):
    """
    Adjust the widths of a seaborn-generated boxplot.
    """

    # iterating through Axes instances
    for ax in g.axes:

        # iterating through axes artists:
        for c in ax.get_children():

            # searching for PathPatches
            if isinstance(c, PathPatch):
                # getting current width of box:
                p = c.get_path()
                verts = p.vertices
                verts_sub = verts[:-1]
                xmin = np.min(verts_sub[:, 0])
                xmax = np.max(verts_sub[:, 0])
                xmid = 0.5*(xmin+xmax)
                xhalf = 0.5*(xmax - xmin)

                # setting new width of box
                xmin_new = xmid-fac*xhalf
                xmax_new = xmid+fac*xhalf
                verts_sub[verts_sub[:, 0] == xmin, 0] = xmin_new
                verts_sub[verts_sub[:, 0] == xmax, 0] = xmax_new

                # setting new width of median line
                for l in ax.lines:
                    if np.all(l.get_xdata() == [xmin, xmax]):
                        l.set_xdata([xmin_new, xmax_new])


### Import Data
DataMatrix = pd.read_excel(r'/Users/lauramedlock 1/Desktop/Modeling-Projects/SDH-Model/Figures/Figure 3/Figure3C-Data-CandF-Dis.xlsx')  #,sheet_name='Avg(Log)'
#DataMatrix = pd.read_excel(r'/Users/lauramedlock 1/Desktop/Modeling-Projects/SDH-Model/GA/disinhibition/Cand10-Dis.xlsx')

# Figure 1A (PAN Scaling)
# fig, ax = plt.subplots(1, sharex=False, figsize=(4.5*cm, 3.5*cm), dpi=1200)
# forces = DataMatrix.iloc[0,1:15]
# scale = DataMatrix.iloc[[1,2],1:15]
# clr = ['grey','black']
# for i in range(0,len(scale)):
#     plt.plot(forces,scale.iloc[i], "-", color=clr[i], linewidth=1.0, markersize=2)
#     ax.set_ylim(-0.1,1.05)
#     ax.set_yticks([0,1])
#     ax.set_xscale('log')
#     ax.set_xticks([0,5,10,20,50,100,200,400])
#     ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
#     ax.set_xlim(0,400)
#     ax.set(xlabel='Mechanical Force (mN)', ylabel='Scale Factor')
# Figure 1A (PAN FIRING)
# fig, ax = plt.subplots(1, sharex=False, figsize=(4.5*cm, 3.5*cm), dpi=1200)
# forces = DataMatrix.iloc[0,1:15]
# scale = DataMatrix.iloc[[1,2,3],1:15]
# clr = ['#986632','#666733','#cb9932']
# for i in range(0,len(scale)):
#     plt.plot(forces,scale.iloc[i], "-", color=clr[i], linewidth=1.0, markersize=2)
#     ax.set_ylim(-1,20)
#     ax.set_yticks([0,5,10,15,20])
#     ax.set_xscale('log')
#     ax.set_xticks([0,5,10,20,50,100,200,400])
#     ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
#     ax.set_xlim(0,410)
#     ax.set(xlabel='Mechanical Force (mN)', ylabel='Average Firing Rate (spk/s)')

# Plotting Figure 2:
#fig, ax = plt.subplots(1, sharex=False, figsize=(7*cm, 6*cm), dpi=1200) # fig 2
# # my_pal = {"Exp":"grey","Sim":"w"} # for figure 3
# # my_pal2 = {"Exp":"grey","Sim":"w"} # for figure 3
# ax = plt.plot(x_coordinates, y_coordinates,linestyle='dashed',linewidth=1)
# ax = sns.boxplot(x="Mechanical Force", y="Firing Rate", hue='Type', data=DataMatrix, palette=my_pal,dodge=True, showfliers = False,linewidth=0.5) # for figure 3
# ax = sns.stripplot(x="Mechanical Force", y="Firing Rate", hue='Type',data=DataMatrix, palette=my_pal2,edgecolor="black",jitter=False,dodge=True,size=3,linewidth=0.5)
# ax.set_yticks([0,10,20,30,40,50,60,70,80,90])
# #ax.set_xticklabels(labels=["50 mN","100 mN","200 mN"])
# ax.set(xlabel='Mechanical Force (mN)', ylabel='Firing Rate of pNK1 Neurons (spk/s)')
# # #ax.legend_.set_title(None)
# ax.set_ylim([-5,90])
# ax.legend_.remove()


## NEW Figure 3B/C (little boxplots) 
fig, ax = plt.subplots(1, sharex=False, figsize=(3.5*cm, 3.8*cm), dpi=1200)  
my_pal = {"Control":"w","Dis":"w"} 
my_pal2 = {"Control":"w","Dis":"r"}
val = [0,1,2,3,4]
ctrl = [0,0,1.5,2.3,11]
dis = [0,20.9,101.5,116,143.3]
ax = plt.plot(val, dis,linewidth=1)
x_coordinates = [-0.5, 9.5] # plot line at median
y_coordinates = [30, 30] # plot line at median
ax = plt.plot(x_coordinates, y_coordinates,linestyle='dashed',linewidth=1)
ax = sns.boxplot(x="Mechanical Force", y="Firing Rate", hue='Type', data=DataMatrix, palette=my_pal,dodge=True, showfliers = False,linewidth=0.5) 
ax = sns.stripplot(x="Mechanical Force", y="Firing Rate", hue='Type',data=DataMatrix, palette=my_pal2,marker="^",edgecolor="black",jitter=False,dodge=True,size=3,linewidth=0.5)
ax.set_yticks([0,100,200,300])
ax.set_xticklabels(labels=["10","25","50","100","200"])
ax.set_yticklabels(labels=["0","XX","XX","XX"])
ax.set(xlabel='', ylabel='')
ax.set_ylim([-5,350])
ax.legend_.remove()
## New Figure 3D (boxplots)
# fig, ax = plt.subplots(1, sharex=False, figsize=(6*cm, 5*cm), dpi=1200)  
# my_pal = {"C":"#444444","Ab":"#b2b2b2"} 
# my_pal2 = {"C":"#444444","Ab":"#b2b2b2"} 
# ax = sns.boxplot(x='WeightType',y='Weight', hue='Group', hue_order ={'Ab','C'}, data=DataMatrix, palette=my_pal,linewidth=0.5,showfliers = False) 
# ax = sns.stripplot(x='WeightType',y='Weight', hue='Group', hue_order ={'Ab','C'}, data=DataMatrix,palette=my_pal2,size=5,jitter=False,edgecolor="black",linewidth=0.5,dodge=True) 
# ax.set_ylim([-8,0.1])
# ax.set_yticks([-7,-5,-3,-1])
# ax.legend_.remove()
# ax.set_xticklabels(labels=["Aβ→E","C/Aδ→E","E→pNK1","E→E","I→E"],rotation=30)
# ax.set(xlabel='', ylabel='Average Weight (log)')
## New Figure 3E (regression + scatter)
# fig, ax = plt.subplots(2,2, sharex=False, figsize=(6*cm, 5.5*cm), dpi=1200)  
# my_pal = {"C":"#444444","AB":"#b2b2b2"} 
# sns.scatterplot(ax=ax[1,1],data=DataMatrix, x="AbtoE2", y="EtoNK1B",hue="Group",palette=my_pal,linewidth=0.5,edgecolor='k',size=1)
# sns.regplot(ax=ax[1,1],data=DataMatrix, x="AbtoE2", y="EtoNK1B",scatter=False,ci=None,color='k',truncate=False,line_kws={'linewidth':1.5})
# sns.scatterplot(ax=ax[1,0],data=DataMatrix, x="AbtoE1", y="EtoNK1B",hue="Group",palette=my_pal,linewidth=0.5,edgecolor='k',size=1)
# sns.regplot(ax=ax[1,0],data=DataMatrix, x="AbtoE1", y="EtoNK1B",scatter=False,ci=None,color='k',truncate=False,line_kws={'linewidth':1.5})
# sns.scatterplot(ax=ax[0,1],data=DataMatrix, x="AbtoE2", y="EtoNK1A",hue="Group",palette=my_pal,linewidth=0.5,edgecolor='k',size=1)
# sns.regplot(ax=ax[0,1],data=DataMatrix, x="AbtoE2", y="EtoNK1A",scatter=False,ci=None,color='k',truncate=False,line_kws={'linewidth':1.5})
# sns.scatterplot(ax=ax[0,0],data=DataMatrix, x="AbtoE1", y="EtoNK1A",hue="Group",palette=my_pal,linewidth=0.5,edgecolor='k',size=1)
# sns.regplot(ax=ax[0,0],data=DataMatrix, x="AbtoE1", y="EtoNK1A",scatter=False,ci=None,color='k',truncate=False,line_kws={'linewidth':1.5})
# ## axis settings
# ax[0,0].set_ylim([-9,0.5])
# ax[0,0].set_xlim([-9,0.5])
# ax[0,0].set_xticks([-8,-6,-4,-2,0])
# ax[0,0].set_yticks([-8,-6,-4,-2,0])
# ax[0,0].set_xticklabels(labels=['','','','',''])
# ax[0,0].legend_.remove()
# ax[0,0].set(xlabel='', ylabel='AMPA')
# ax[0,1].set_ylim([-9,0.5])
# ax[0,1].set_xlim([-9,0.5])
# ax[0,1].set_xticks([-8,-6,-4,-2,0])
# ax[0,1].set_yticks([-8,-6,-4,-2,0])
# ax[0,1].set_yticklabels(labels=['','','','',''])
# ax[0,1].set_xticklabels(labels=['','','','',''])
# ax[0,1].legend_.remove()
# ax[0,1].set(xlabel='', ylabel='')
# ax[1,0].set_ylim([-9,0.5])
# ax[1,0].set_xlim([-9,0.5])
# ax[1,0].set_xticks([-8,-6,-4,-2,0])
# ax[1,0].set_yticks([-8,-6,-4,-2,0])
# ax[1,0].legend_.remove()
# ax[1,0].set(xlabel='AMPA', ylabel='NMDA')
# ax[1,1].set_ylim([-9,0.5])
# ax[1,1].set_xlim([-9,0.5])
# ax[1,1].set_xticks([-8,-6,-4,-2,0])
# ax[1,1].set_yticks([-8,-6,-4,-2,0])
# ax[1,1].set_yticklabels(labels=['','','','',''])
# ax[1,1].legend_.remove()
# ax[1,1].set(xlabel='NMDA', ylabel='')
## New Figure 3E (scatter):
# fig, ax = plt.subplots(1, sharex=False, figsize=(5*cm, 4.5*cm), dpi=1200)  
# my_pal = {'Control':'white','AMPA-5D':'#00ccff','AMPA-5U':'#00ccff','NMDA-5D':'#0000ff','NMDA-5U':'#0000ff','NK1-5D':'#6d6e71','NK1-5U':'#6d6e71','GABA-5D':'#ff0000','GABA-5U':'#ff0000','Gly-5D':'#ff99cc','Gly-5U':'#ff99cc'} 
# ax = sns.stripplot(x="Force", y="Observed", hue='Condition',data=DataMatrix, palette=my_pal,edgecolor="black",jitter=True,dodge=False,size=5,linewidth=0.5)
# #sns.scatterplot(data=DataMatrix, x="Predicted", y="Observed",hue="Condition",palette=my_pal,linewidth=0.5,edgecolor='k',size=1)
# ax.axhline(0) # Q1 of 50mN
# ax.axhline(0.4) #median of 50mN
# ax.axhline(1.75) # Q3 of 50mN
# ax.axhline(1.3) # Q1 of 100mN
# ax.axhline(3) #median of 100mN
# ax.axhline(5.85) # Q3 of 100mN
# ax.axhline(7.85) # Q1 of 200mN
# ax.axhline(11.3) #median of 200mN
# ax.axhline(13.7) # Q3 of 200mN
# ax.legend_.remove()
# ax.set_ylim([-1,18])
# # ax.set_xlim([-1,18])
# ax.set_xticklabels(labels=['50','100','200'])
# ax.set(xlabel='', ylabel='pNK1 Firing Rate (spk/s)')

# OLD Figure (sensitivity):
# fig, ax = plt.subplots(1, sharex=False, figsize=(10*cm, 7*cm), dpi=1200)
# my_pal2 = {'Control':'white','AMPA-5D':'#7DAB55','AMPA-5U':'#B1CE95','NMDA-5D':'#4273AF','NMDA-5U':'#A3C0E3','NK1-5D':'#9477cb','NK1-5U':'#cec1e7','GABA-5D':'#D64546','GABA-5U':'#EE8079','Gly-5D':'#F5C243','Gly-5U':'#FBE7A2'} 
# ax = sns.boxplot(x="Force", y="Firing Rate",hue="Condition", data=DataMatrix, color='w',palette=my_pal2, showfliers = False)
# #ax = sns.stripplot(x="Force", y="Firing Rate",hue="Condition", data=DataMatrix,palette=my_pal2,size=5,jitter=False,edgecolor="black",linewidth=0.5,dodge=True)
# ax.set(xlabel='', ylabel='Firing Rate of pNK1 Neurons (spk/s)')
# ax.set_ylim([-2,35])
# ax.set_xticklabels(labels=["50 mN","100 mN","200 mN"])
# adjust_box_widths(fig, 0.8)
# ax.legend_.remove()

#Plotting Figure 4B:
# fig, ax = plt.subplots(1, sharex=False, figsize=(8*cm, 5*cm), dpi=1200)
# my_pal = {"#000000","#b2b2b2"}
# ax = sns.boxplot(x="Mechanical Force", y="Firing Rate", data=DataMatrix, color='w', showfliers = False)
# ax = sns.stripplot(x="Mechanical Force", y="Firing Rate",hue="Force", data=DataMatrix,palette=my_pal,size=5,jitter=False,edgecolor="black",linewidth=0.5)
# ax.set(xlabel='', ylabel='Firing Rate of pNK1 Neurons (spk/s)')
# ax.set_ylim([-5,100])
# ax.set_xticklabels(labels=["Control","–PV","–PV\n–PKCγ","–PV\n–DOR","–PV\n–SOM","-All","Control","–PV","–PV\n–PKCγ","–PV\n–DOR","–PV\n–SOM","-All",])
# ax.legend_.remove()
#Plotting Fig 6C:
# fig, ax = plt.subplots(1, sharex=False, figsize=(3.8*cm, 6*cm), dpi=1200)
# forces = [0, 20, 50, 100, 200]
# medians = DataMatrix.iloc[0:6,1:6]
# for i in range(0,len(forces)+1):
#     plt.plot(forces,medians.iloc[i], "k-o", linewidth=1.0, markersize=2)
#     ax.set_ylim(-5,80)
#     ax.set_xlim(-25,225)
#     ax.set_xticks([0,50,100,150,200])
#     ax.set(xlabel='Mechanical Force (mN)', ylabel='Median pNK1 Firing Rate (spk/s)')


## Plotting Figure 5A/C:
# fig, ax = plt.subplots(1, sharex=False, figsize=(7.5*cm, 5*cm), dpi=1200)
# my_pal = {"Control":"white","DYN-":"#FF0000","PV-":"#EF85A9"}  # "VGLUT3-":"#6699FF","CR-":"#9966FF"
# my_pal2 = {"Control":"white","DYN-":"white","PV-":"white"}  # "VGLUT3-":"white","CR-":"white"
# ax = sns.boxplot(x="Stimulus Intensity", y="Firing Rate", hue="Mechanical Force", palette = my_pal2, data=DataMatrix, color='w',showfliers = False)
# ax = sns.stripplot(x="Stimulus Intensity", y="Firing Rate", hue="Mechanical Force", data=DataMatrix,palette=my_pal,size=5,edgecolor="black",jitter=False,linewidth=0.5,dodge=True)
# ax.set_xticklabels(labels=["20 mN","50 mN","100 mN","200 mN"])
# ax.set_ylim([-5,100])
# ax.set_yticks([0,25,50,75,100])
# ax.set(xlabel='', ylabel='Firing Rate of pNK1 Neurons (spk/s)')
# ax.legend_.remove()
## Plotting Figure 5B - top:
# fig, ax = plt.subplots(1, 5, sharex=True, figsize=(17*cm, 4*cm), dpi=1200)
# my_pal = {"50mN":"#aaaaaa","100mN":"#777777","200mN":"#333333"}
# dataPV0 = DataMatrix.loc[DataMatrix['PV'] == 0]
# dataPV20 = DataMatrix.loc[DataMatrix['PV'] == 20]
# dataPV40 = DataMatrix.loc[DataMatrix['PV'] == 40]
# dataPV60 = DataMatrix.loc[DataMatrix['PV'] == 60]
# dataPV80 = DataMatrix.loc[DataMatrix['PV'] == 80]
# sns.lineplot(ax=ax[4],data=dataPV0, x="Index", y="Response",hue="Stimulus Intensity",style="Stimulus Intensity",style_order=["200mN","100mN","50mN"], palette=my_pal,linewidth=1,sort=True)
# ax[4].hlines(y=0, xmin=0, xmax=7.5, linewidth=0.5, color='r',linestyle='-')
# sns.lineplot(ax=ax[3],data=dataPV20, x="Index", y="Response",hue="Stimulus Intensity",style="Stimulus Intensity",style_order=["200mN","100mN","50mN"], palette=my_pal,linewidth=1,sort=True)
# ax[3].hlines(y=0, xmin=0, xmax=7.5, linewidth=0.5, color='r',linestyle='-')
# sns.lineplot(ax=ax[2],data=dataPV40, x="Index", y="Response",hue="Stimulus Intensity",style="Stimulus Intensity",style_order=["200mN","100mN","50mN"], palette=my_pal,linewidth=1,sort=True)
# ax[2].hlines(y=0, xmin=0, xmax=7.5, linewidth=0.5, color='r',linestyle='-')
# sns.lineplot(ax=ax[1],data=dataPV60, x="Index", y="Response",hue="Stimulus Intensity",style="Stimulus Intensity",style_order=["200mN","100mN","50mN"], palette=my_pal,linewidth=1,sort=True)
# ax[1].hlines(y=0, xmin=0, xmax=7.5, linewidth=0.5, color='r',linestyle='-')
# sns.lineplot(ax=ax[0],data=dataPV80, x="Index", y="Response",hue="Stimulus Intensity",style="Stimulus Intensity",style_order=["200mN","100mN","50mN"], palette=my_pal,linewidth=1,sort=True)
# ax[0].hlines(y=0, xmin=0, xmax=7.5, linewidth=0.5, color='r',linestyle='-')
# # axis settings
# ax[0].set_ylim([-8,65])
# ax[0].set_xlim([0,7.5])
# ax[0].set_xticks([1,2,3,4,5,6,7])
# ax[0].set_xticklabels(labels=["C","1x","10x","25x","50x","100x","200x"],rotation=45)
# ax[0].set_yticks([0,20,40,60])
# ax[0].set(xlabel='', ylabel='Δ in Median pNK1\nFiring Rate (spk/s)')
# ax[0].legend_.remove()
# ax[1].set(xlabel='', ylabel='')
# ax[1].set_ylim([-8,65])
# ax[1].set_xlim([0,7.5])
# ax[1].set_xticks([1,2,3,4,5,6,7])
# ax[1].set_xticklabels(labels=["C","1x","10x","25x","50x","100x","200x"],rotation=45)
# ax[1].set_yticks([0,20,40,60])
# ax[1].set_yticklabels(labels=["","","",""])
# ax[1].legend_.remove()
# ax[2].set(xlabel='', ylabel='')
# ax[2].set_ylim([-8,65])
# ax[2].set_xlim([0,7.5])
# ax[2].set_xticks([1,2,3,4,5,6,7])
# ax[2].set_xticklabels(labels=["C","1x","10x","25x","50x","100x","200x"],rotation=45)
# ax[2].set_yticks([0,20,40,60])
# ax[2].set_yticklabels(labels=["","","",""])
# ax[2].legend_.remove()
# ax[3].set(xlabel='', ylabel='')
# ax[3].set_ylim([-8,65])
# ax[3].set_xlim([0,7.5])
# ax[3].set_xticks([1,2,3,4,5,6,7])
# ax[3].set_xticklabels(labels=["C","1x","10x","25x","50x","100x","200x"],rotation=45)
# ax[3].set_yticks([0,20,40,60])
# ax[3].set_yticklabels(labels=["","","",""])
# ax[3].legend_.remove()
# ax[4].set(xlabel='', ylabel='')
# ax[4].set_ylim([-8,65])
# ax[4].set_xlim([0,7.5])
# ax[4].set_xticks([1,2,3,4,5,6,7])
# ax[4].set_xticklabels(labels=["C","1x","10x","25x","50x","100x","200x"],rotation=45)
# ax[4].set_yticks([0,20,40,60])
# ax[4].set_yticklabels(labels=["","","",""])
# ax[4].legend_.remove()
## Plotting Figure 7B - bottom:
# fig, ax = plt.subplots(1, 5, sharex=True, figsize=(17*cm, 4*cm), dpi=1200)
# my_pal = {"50mN":"#aaaaaa","100mN":"#777777","200mN":"#333333"}
# dataPV0 = DataMatrix.loc[DataMatrix['PV'] == 0]
# dataPV20 = DataMatrix.loc[DataMatrix['PV'] == 20]
# dataPV40 = DataMatrix.loc[DataMatrix['PV'] == 40]
# dataPV60 = DataMatrix.loc[DataMatrix['PV'] == 60]
# dataPV80 = DataMatrix.loc[DataMatrix['PV'] == 80]
# sns.boxplot(ax=ax[4],x="Stimulus Intensity", y="Firing Rate", data=dataPV0, color='w', showfliers = False,linewidth=0.5)
# sns.stripplot(ax=ax[4],x="Stimulus Intensity", y="Firing Rate",hue="Stimulus Intensity", data=dataPV0,palette=my_pal,size=5,jitter=False,edgecolor="black",linewidth=0.5,dodge=False)
# sns.boxplot(ax=ax[3],x="Stimulus Intensity", y="Firing Rate", data=dataPV20, color='w', showfliers = False,linewidth=0.5)
# sns.stripplot(ax=ax[3],x="Stimulus Intensity", y="Firing Rate",hue="Stimulus Intensity", data=dataPV20,palette=my_pal,size=5,jitter=False,edgecolor="black",linewidth=0.5,dodge=False)
# sns.boxplot(ax=ax[2],x="Stimulus Intensity", y="Firing Rate", data=dataPV40, color='w', showfliers = False,linewidth=0.5)
# sns.stripplot(ax=ax[2],x="Stimulus Intensity", y="Firing Rate",hue="Stimulus Intensity", data=dataPV40,palette=my_pal,size=5,jitter=False,edgecolor="black",linewidth=0.5,dodge=False)
# sns.boxplot(ax=ax[1],x="Stimulus Intensity", y="Firing Rate", data=dataPV60, color='w', showfliers = False,linewidth=0.5)
# sns.stripplot(ax=ax[1],x="Stimulus Intensity", y="Firing Rate",hue="Stimulus Intensity", data=dataPV60,palette=my_pal,size=5,jitter=False,edgecolor="black",linewidth=0.5,dodge=False)
# sns.boxplot(ax=ax[0],x="Stimulus Intensity", y="Firing Rate", data=dataPV80, color='w', showfliers = False,linewidth=0.5)
# sns.stripplot(ax=ax[0],x="Stimulus Intensity", y="Firing Rate",hue="Stimulus Intensity", data=dataPV80,palette=my_pal,size=5,jitter=False,edgecolor="black",linewidth=0.5,dodge=False)
# ax[0].set_ylim([-5,30])
# ax[0].set_xticklabels(labels=["50","100","200"])
# ax[0].set_yticks([0,10,20,30])
# ax[0].set(xlabel='', ylabel='Firing Rate of\npNK1 Neurons (spk/s)')
# ax[0].legend_.remove()
# ax[1].set(xlabel='', ylabel='')
# ax[1].set_ylim([-5,30])
# ax[1].set_xticklabels(labels=["50","100","200"])
# ax[1].set_yticks([0,10,20,30])
# ax[1].set_yticklabels(labels=["","","",""])
# ax[1].legend_.remove()
# ax[2].set(xlabel='', ylabel='')
# ax[2].set_ylim([-5,30])
# ax[2].set_xticklabels(labels=["50","100","200"])
# ax[2].set_yticklabels(labels=["","","",""])
# ax[2].set_yticks([0,10,20,30])
# ax[2].legend_.remove()
# ax[3].set(xlabel='', ylabel='')
# ax[3].set_ylim([-5,30])
# ax[3].set_yticks([0,10,20,30])
# ax[3].set_xticklabels(labels=["50","100","200"])
# ax[3].set_yticklabels(labels=["","","",""])
# ax[3].legend_.remove()
# ax[4].set(xlabel='', ylabel='')
# ax[4].set_ylim([-5,30])
# ax[4].set_yticks([0,10,20,30])
# ax[4].set_xticklabels(labels=["50","100","200"])
# ax[4].set_yticklabels(labels=["","","",""])
# ax[4].legend_.remove()
# plt.setp(ax[0].lines, color='k', linewidth=0.5)
# plt.setp(ax[0].artists, edgecolor='k',linewidth=0.5)
# plt.setp(ax[1].lines, color='k', linewidth=0.5)
# plt.setp(ax[1].artists, edgecolor='k',linewidth=0.5)
# plt.setp(ax[2].lines, color='k', linewidth=0.5)
# plt.setp(ax[2].artists, edgecolor='k',linewidth=0.5)
# plt.setp(ax[3].lines, color='k', linewidth=0.5)
# plt.setp(ax[3].artists, edgecolor='k',linewidth=0.5)
# plt.setp(ax[4].lines, color='k', linewidth=0.5)
# plt.setp(ax[4].artists, edgecolor='k',linewidth=0.5)
## Plotting Figure 7D:
# fig, ax = plt.subplots(1, sharex=False, figsize=(2*cm, 5*cm), dpi=1200)
# my_pal = {"Control":"#000000","DYN-":"#FF0000","VGLUT3-":"#6699FF","CR-":"#9966FF"}
# my_pal2 = {"Control":"white","DYN-":"white","VGLUT3-":"white","CR-":"white"}
# ax = sns.boxplot(x="Stimulus Intensity", y="Firing Rate", hue="Mechanical Force", palette = my_pal2, data=DataMatrix, color='w',showfliers = False)
# ax = sns.stripplot(x="Stimulus Intensity", y="Firing Rate", hue="Mechanical Force", data=DataMatrix,palette=my_pal,size=5,edgecolor="black",jitter=False,linewidth=0.5,dodge=True)
# ax.set_xticklabels(labels=["20 mN"])
# ax.set_ylim([-5,100])
# ax.set_yticks([0,25,50,75,100])
# ax.set(xlabel='', ylabel='Firing Rate of pNK1 Neurons (spk/s)')
# ax.legend_.remove()

## Figure 6A (IRB):
# fig, ax = plt.subplots(1, sharex=False, figsize=(11*cm, 6*cm), dpi=1200) 
# my_pal = {"Control":"w","90% IRB":"#ff0000","100% IRB":"#595959"}
# my_pal2 = {"Control":"w","90% IRB":"#ff0000","100% IRB":"#595959"} # pink: #ff4c66
# x_coordinates = [-0.5, 9.5] # plot line at median
# y_coordinates = [30, 30] # plot line at median
# ax = plt.plot(x_coordinates, y_coordinates,linestyle='dashed',linewidth=1)
# ax = sns.boxplot(x="Mechanical Force", y="Firing Rate", hue='Type', data=DataMatrix, palette=my_pal,dodge=True, showfliers = False,linewidth=0.5)
# ax = sns.stripplot(x="Mechanical Force", y="Firing Rate", hue='Type',data=DataMatrix, palette=my_pal2,edgecolor="black",jitter=False,dodge=True,size=3,linewidth=0.5)
# ax.set_yticks([0,10,20,30,40,50,60,70,80,90])
# ax.set_xticklabels(labels=["0","5","10","15","20","25","30","50","100","200"])
# ax.set(xlabel='', ylabel='')
# ax.set(xlabel='Mechanical Force (mN)', ylabel='Firing Rate of pNK1 Neurons (spk/s)')
# ax.set_ylim([-5,90])
# ax.legend_.remove()
# Figure 6B/D (CD and CDPV):
# fig, ax = plt.subplots(1, sharex=False, figsize=(4*cm, 4*cm), dpi=1200)  
# my_pal = {'CD':'#ffc300','CDPV':'#b266b2'} 
# val = [0,1,2,3]
# ctrl = [0,0,0.4,11.3]
# dis = [0,9.3,59.8,68]
# ax = sns.boxplot(x="Force", y="Firing Rate", hue='Change',data=DataMatrix, palette=my_pal,dodge=True, showfliers = False,linewidth=0.5)
# ax = sns.stripplot(x="Force", y="Firing Rate", hue='Change',data=DataMatrix, palette=my_pal,edgecolor="black",jitter=False,dodge=False,size=5,linewidth=0.5)
# ax = sns.lineplot(x=val,y=ctrl,linewidth=0.5)
# ax = sns.lineplot(x=val,y=dis,linewidth=0.5)
# ax.legend_.remove()
# ax.set_ylim([-5,75])
# ax.set_yticks([0,25,50,75])
# ax.set_xticklabels(labels=['10','20','50','200'])
# ax.set(xlabel='', ylabel='pNK1 Firing Rate (spk/s)')
# # Plot Figure 6C:
# fig, ax = plt.subplots(1, sharex=False, figsize=(7.5*cm, 3.8*cm), dpi=1200)
# my_pal = {"Control":"white", "IRB":"#ff0000","CD":"#ffc300","CDPV":"#b266b2"}
# my_pal2 = {"Control":"white", "IRB":"#ff0000","CD":"#ffc300","CDPV":"#b266b2"}
# order1 = ['iPV','iISLET','iDYN','eVGLUT3','ePKC','eDOR','eTrC','eSST','eCR']
# ax = sns.boxplot(x="Interneuron", y="Firing Rate",hue="Condition",order=order1,data=DataMatrix,orient="v", palette=my_pal, showfliers = False)
# #ax = sns.stripplot(x="Interneuron", y="Firing Rate",hue="Condition",data=DataMatrix,size=4,palette=my_pal2,jitter=False,edgecolor="black",dodge=True,linewidth=0.5)
# ax.set(xlabel='', ylabel='Firing Rate (spk/s)')
# ax.set_ylim([-5,150])
# ax.set_yticks([0,25,50,75,100,125,150])
# ax.set_yticklabels(labels=['0','25','50','75','xx','xx','xx'])
# # ax.set_ylim([-5,75])
# # ax.set_yticks([0,25,50,75])
# ax.set_xticklabels(labels=['','','','','','','','',''])
# # ax.set_xticklabels(labels=order1,rotation=45)
# ax.legend_.remove()

# # OLD CHLORIDE DYSREG FIGURE:
# fig, ax = plt.subplots(1, sharex=False, figsize=(6.6*cm, 6*cm), dpi=1200)
# # my_pal = {"Control":"white", "Ten":"#c4c5c6","Twenty":"#767676"}
# # my_pal2 = {"Control":"white", "Ten":"#c4c5c6","Twenty":"#767676"}
# my_pal = {"Control":"white", "Global":"#d2d2d2","Excitatory":"#3540f4","Inhibitory":"#D62728"}
# my_pal2 = {"Control":"white", "Global":"#d2d2d2","Excitatory":"#3540f4","Inhibitory":"#D62728"}
# ax = sns.boxplot(x="Force", y="Firing Rate",hue="Change",data=DataMatrix,palette=my_pal, showfliers = False)
# ax = sns.stripplot(x="Force", y="Firing Rate",hue="Change",data=DataMatrix,size=4,palette=my_pal2,jitter=False,edgecolor="black",dodge=True,linewidth=0.5)
# ax.set(xlabel='Mechanical Force (mN)', ylabel='Firing Rate of pNK1 Neurons (spk/s)')
# ax.set_ylim([-5,80])
# ax.set_yticks([0,10,20,30,40,50,60,70,80])
# ax.set_xticklabels(labels=["25","50","200"])
# ax.legend_.remove()
# Plot Figure 8C:
# col1 = "orchid"
# col2 = "slateblue"
# fig, ax = plt.subplots(1, sharex=False, figsize=(5.5*cm, 6.5*cm), dpi=1200)
# my_pal = {col1}
# my_pal3 = {"black"}
# ax = sns.boxplot(x="Force", y="Change",data=DataMatrix,palette=my_pal, showfliers = False)
# ax = sns.stripplot(x="Force", y="Change",data=DataMatrix,size=4,palette=my_pal,jitter=False,edgecolor="black",dodge=True,linewidth=0.5)
# ax.set(xlabel='Mechanical Force (mN)', ylabel='% Increase in pNK1 Firing Rate')
# ax.set_ylim([-5,80])
# ax.tick_params(axis='y', colors=col1)
# ax.yaxis.label.set_color(col1)
# ax2 = ax.twinx()
# my_pal2 = {col2}
# ax2 = sns.boxplot(x="Force", y="Difference",data=DataMatrix,palette=my_pal2, showfliers = False)
# ax2 = sns.stripplot(x="Force", y="Difference",data=DataMatrix,size=4,palette=my_pal2,jitter=False,edgecolor="black",dodge=True,linewidth=0.5)
# ax2.set(xlabel='Mechanical Force (mN)', ylabel='Increase in pNK1 Firing Rate (spk/s)')
# ax2.set_ylim([-0.6,10])
# ax2.set_xlim([-1,8])
# ax2.set_xticklabels(labels=["25","25","50","50","200","200"])
# ax2.tick_params(axis='y', colors=col2)
# ax2.yaxis.label.set_color(col2)
# ax2.set_xticks([0,1,3,4,6,7])
# adjust_box_widths(fig,1.2)
# for axis in ['left']:
#   ax.spines[axis].set_linewidth(1.0)
#   ax.spines[axis].set_color(col1)
# for axis in ['right']:
#   ax2.spines[axis].set_linewidth(1.0)
#   ax2.spines[axis].set_color(col2)

#Plotting Figure 7B (NK1 BLOCK):
# fig, ax = plt.subplots(1, sharex=False, figsize=(8.5*cm, 6*cm), dpi=1200)
# my_pal = {"20mN":"#b2b2b2","200mN":"black"}
# ax = sns.boxplot(x="Mechanical Force", y="Firing Rate", data=DataMatrix, color='w', showfliers = False)
# ax = sns.stripplot(x="Mechanical Force", y="Firing Rate",hue="Force", data=DataMatrix,palette=my_pal,size=5,jitter=False,edgecolor="black",linewidth=0.5)
# ax.set(xlabel='', ylabel='Firing Rate of pNK1 Neurons (spk/s)')
# ax.set_ylim([-5,90])
# ax.set_yticks([0,10,20,30,40,50,60,70,80,90])
# ax.set_xticklabels(labels=["Control","NK1R-","GABAR-\nGlyR-","GABAR-\nGlyR-\nCNK1-","GABAR-\nGlyR-\nSSTNK1-","GABAR-\nGlyR-\nCRNK1-","GABAR-\nGlyR-\nAllNK1-","Control","NK1R-","GABAR-\nGlyR-","GABAR-\nGlyR-\nCNK1-","GABAR-\nGlyR-\nSSTNK1-","GABAR-\nGlyR-\nCRNK1-","GABAR-\nGlyR-\nAllNK1-"])
# ax.legend_.remove()

# Plot Figure 8A&B (KA SIMULATIONS):
# fig, ax = plt.subplots(1, sharex=False, figsize=(8*cm, 5*cm), dpi=1200)
# my_pal = {"#b2b2b2"} # for 25mN
# #my_pal = {"#000000"} # for 200mN
# ax = sns.boxplot(x="Baseline", y="Firing Rate", data=DataMatrix,color='w', width=0.6, dodge=True, showfliers = False)
# ax = sns.stripplot(x="Baseline", y="Firing Rate",data=DataMatrix, palette=my_pal, jitter=False, size=4,edgecolor="black",dodge=True,linewidth=0.5)
# ax.set(xlabel='',ylabel='')
# ax.set_xticklabels(labels=["0","20","40","60","80","100","120","140","160"])
# ax.set_ylim([-5,140])
# ax.set_yticks([0,70,140])
# #Plot Figure 11C:
# fig, ax = plt.subplots(1, sharex=False, figsize=(8.8*cm, 5*cm), dpi=1200)
# my_pal = {"20mN":"#b2b2b2","200mN":"black"}
# ax = sns.boxplot(x="Mechanical Force", y="Firing Rate", data=DataMatrix, color='w', showfliers = False)
# ax = sns.stripplot(x="Mechanical Force", y="Firing Rate",hue="Force", data=DataMatrix,palette=my_pal,size=5,jitter=False,edgecolor="black",linewidth=0.5)
# ax.set(xlabel='', ylabel='Firing Rate of pNK1 Neurons (spk/s)')
# ax.set_ylim([-5,100])
# ax.set_yticks([0,20,40,60,80,100])
# ax.set_xticklabels(labels=["Control","IRB","IRB\n+110","IRB\n+150","IRB\n+180","Control","IRB","IRB\n+110","IRB\n+150","IRB\n+180"])
# ax.legend_.remove()

# General plot settings
sns.despine(fig=None)
plt.setp(ax.lines, color='k', linewidth=0.5) 
plt.setp(ax.artists, edgecolor='k',linewidth=0.5)
for axis in ['left','bottom']:
  ax.spines[axis].set_linewidth(0.5)
  ax.spines[axis].set_color('k')  
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)

plt.tight_layout()

# Saving Figures:
fig.savefig('Figure3C-CandF.svg', format='svg', dpi=1200)
fig.savefig('Figure3C-CandF.png', format='png', dpi=1200)