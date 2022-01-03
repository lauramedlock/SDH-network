#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 09:51:05 2021
@author: lauramed
For plotting figures (Sekiguchi et al. 2021)
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


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
DataMatrix = pd.read_excel(r'/Users/lauramedlock 1/Desktop/Modeling-Projects/SDH-Model/Figures/Figure 9/FigureA-Data-20mN.xlsx')
#DataMatrix = pd.read_excel(r'/Users/lauramedlock 1/Desktop/Modeling-Projects/SDH-Model/GA/disinhibition/Cand10-Dis.xlsx')

# Plotting Figure 3 & 5:
# fig, ax = plt.subplots(1, sharex=False, figsize=(7*cm, 6*cm), dpi=1200) # fig 3
# fig, ax = plt.subplots(1, sharex=False, figsize=(8.5*cm, 7*cm), dpi=1200)  # fig 5
# # my_pal = {"Exp":"grey","Sim":"w"} # for figure 3
# # my_pal2 = {"Exp":"grey","Sim":"w"} # for figure 3
# my_pal = {"Control":"w","90% IRB":"red","100% IRB":"#595959"} # for figure 5
# my_pal2 = {"Control":"w","90% IRB":"red","100% IRB":"#595959"} # for figure 5
# # plot line at median
# x_coordinates = [-0.5, 8.5]
# y_coordinates = [30, 30]
# ax = plt.plot(x_coordinates, y_coordinates,linestyle='dashed',linewidth=1)
# ax = sns.boxplot(x="Mechanical Force", y="Firing Rate", hue='Type', data=DataMatrix, palette=my_pal,dodge=True, showfliers = False,linewidth=0.5) # for figure 3
# ax = sns.stripplot(x="Mechanical Force", y="Firing Rate", hue='Type',data=DataMatrix, palette=my_pal2,edgecolor="black",jitter=False,dodge=True,size=3,linewidth=0.5)
# ax.set_yticks([0,10,20,30,40,50,60,70,80,90])
# ax.set_xticklabels(labels=["0","5","10","15","20","25","50","100","200"])
# #ax.set_xticklabels(labels=["50 mN","100 mN","200 mN"])
# ax.set(xlabel='', ylabel='')
# ax.set(xlabel='Mechanical Force (mN)', ylabel='Firing Rate of pNK1 Neurons (spk/s)')
# # #ax.legend_.set_title(None)
# ax.set_ylim([-5,90])
# ax.legend_.remove()

#Plotting Figure 4 (sensitivity):
# fig, ax = plt.subplots(1, sharex=False, figsize=(10*cm, 7*cm), dpi=1200)
# my_pal2 = {'Control':'white','AMPA-5D':'#7DAB55','AMPA-5U':'#B1CE95','NMDA-5D':'#4273AF','NMDA-5U':'#A3C0E3','NK1-5D':'#9477cb','NK1-5U':'#cec1e7','GABA-5D':'#D64546','GABA-5U':'#EE8079','Gly-5D':'#F5C243','Gly-5U':'#FBE7A2'} 
# ax = sns.boxplot(x="Force", y="Firing Rate",hue="Condition", data=DataMatrix, color='w',palette=my_pal2, showfliers = False)
# #ax = sns.stripplot(x="Force", y="Firing Rate",hue="Condition", data=DataMatrix,palette=my_pal2,size=5,jitter=False,edgecolor="black",linewidth=0.5,dodge=True)
# ax.set(xlabel='', ylabel='Firing Rate of pNK1 Neurons (spk/s)')
# ax.set_ylim([-2,35])
# ax.set_xticklabels(labels=["50 mN","100 mN","200 mN"])
# adjust_box_widths(fig, 0.8)
# ax.legend_.remove()

#Plotting Figure 6B:
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


## Plotting Figure 7A:
# fig, ax = plt.subplots(1, sharex=False, figsize=(8.5*cm, 5*cm), dpi=1200)
# my_pal = {"Control":"white","DYN-":"#FF0000","VGLUT3-":"#6699FF","CR-":"#9966FF"}
# my_pal2 = {"Control":"white","DYN-":"white","VGLUT3-":"white","CR-":"white"}
# ax = sns.boxplot(x="Stimulus Intensity", y="Firing Rate", hue="Mechanical Force", palette = my_pal2, data=DataMatrix, color='w',showfliers = False)
# ax = sns.stripplot(x="Stimulus Intensity", y="Firing Rate", hue="Mechanical Force", data=DataMatrix,palette=my_pal,size=5,edgecolor="black",jitter=False,linewidth=0.5,dodge=True)
# ax.set_xticklabels(labels=["20 mN","50 mN","100 mN","200 mN"])
# ax.set_ylim([-1,40])
# ax.set(xlabel='', ylabel='Firing Rate of pNK1 Neurons (spk/s)')
# ax.legend_.remove()
## Plotting Figure 7B - top:
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
## Plotting Figure 7C:
# fig, ax = plt.subplots(1, sharex=False, figsize=(8.5*cm, 5*cm), dpi=1200)
# my_pal = {"Control":"#000000","DYN-":"#FF0000","VGLUT3-":"#6699FF","CR-":"#9966FF"}
# my_pal2 = {"Control":"white","DYN-":"white","VGLUT3-":"white","CR-":"white"}
# ax = sns.boxplot(x="Stimulus Intensity", y="Firing Rate", hue="Mechanical Force", palette = my_pal2, data=DataMatrix, color='w',showfliers = False)
# ax = sns.stripplot(x="Stimulus Intensity", y="Firing Rate", hue="Mechanical Force", data=DataMatrix,palette=my_pal,size=5,edgecolor="black",jitter=False,linewidth=0.5,dodge=True)
# ax.set_xticklabels(labels=["20 mN","50 mN","100 mN","200 mN"])
# ax.set_ylim([-1,40])
# ax.set(xlabel='', ylabel='Firing Rate of pNK1 Neurons (spk/s)')
# ax.legend_.remove()

# # Plot Figure 8B:
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

#Plotting Figure 9 (OLD):
# fig, ax = plt.subplots(1, sharex=False, figsize=(8.5*cm, 7*cm), dpi=1200)
# #my_pal = {"Control":"white","GABA Gly Block":"white","iPV Ablation":"white","EANION":"white"}  
# my_pal = {"black"}  
# my_pal2 = {"Control":"white","GABA Gly Block":"#595959","iPV Ablation":"#8A8A8A","iDYN Ablation":"#444444","EANION":"#D2D2D2"} 
# ax = sns.boxplot(x="Force", y="Firing Rate",hue="Condition",hue_order=['Control','EANION','GABA Gly Block'], data=DataMatrix, color='w',palette=my_pal2, showfliers = False)
# ax = sns.stripplot(x="Force", y="Firing Rate",hue="Condition",hue_order=['Control','EANION','GABA Gly Block'], data=DataMatrix,palette=my_pal2,size=5,jitter=False,edgecolor="black",linewidth=0.5,dodge=True)
# ax.set(xlabel='Mechanical Force (mN)', ylabel='Firing Rate of pNK1 Neurons (spk/s)')
# ax.set_ylim([-5,100])
# ax.set_xticklabels(labels=["10","25","50","200"])
# ax.legend_.remove()

## Plot Figure 9 (NEW):
fig, ax = plt.subplots(1, sharex=False, figsize=(8.5*cm, 7*cm), dpi=1200)
my_pal = {"Control":"white", "IRB":"red","CD":"pink"}
my_pal2 = {"Control":"white", "IRB":"red","CD":"pink"}
ax = sns.boxplot(x="Force", y="Firing Rate",hue="Change",data=DataMatrix,palette=my_pal, showfliers = False)
ax = sns.stripplot(x="Force", y="Firing Rate",hue="Change",data=DataMatrix,size=4,palette=my_pal2,jitter=False,edgecolor="black",dodge=True,linewidth=0.5)
ax.set(xlabel='Mechanical Force (mN)', ylabel='Firing Rate of pNK1 Neurons (spk/s)')
ax.set_ylim([-5,90])
ax.set_yticks([0,10,20,30,40,50,60,70,80,90])
ax.set_xticklabels(labels=["0","10","20","50","100","200"])
ax.legend_.remove()
# # Plot Figure 9NewB:
# fig, ax = plt.subplots(1, sharex=False, figsize=(11.6*cm, 7*cm), dpi=1200)
# my_pal = {"Normal":"white", "IRB":"red","CD":"pink"}
# my_pal2 = {"Normal":"white", "IRB":"red","CD":"pink"}
# order1 = ['iPV','iISLET','iDYN','eVGLUT3','ePKC','eDOR','eTrC','eSST','eCR','pNK1']
# ax = sns.boxplot(x="Interneuron", y="Firing Rate",hue="Condition",order=order1,data=DataMatrix, palette=my_pal, showfliers = False)
# #ax = sns.stripplot(x="Interneuron", y="Firing Rate",hue="Condition",data=DataMatrix,size=4,palette=my_pal2,jitter=False,edgecolor="black",dodge=True,linewidth=0.5)
# ax.set(xlabel='Interneuron Population', ylabel='Firing Rate (spk/s)')
# ax.set_ylim([-5,200])
# ax.set_yticks([0,50,100,150,200])
# ax.set_xticklabels(labels=order1,rotation=45)
# ax.legend_.remove()

#Plotting Figure 10B:
# fig, ax = plt.subplots(1, sharex=False, figsize=(8.5*cm, 6*cm), dpi=1200)
# my_pal = {"20mN":"grey","200mN":"black"}
# ax = sns.boxplot(x="Mechanical Force", y="Firing Rate", data=DataMatrix, color='w', showfliers = False)
# ax = sns.stripplot(x="Mechanical Force", y="Firing Rate",hue="Force", data=DataMatrix,palette=my_pal,size=5,jitter=False,edgecolor="black",linewidth=0.5)
# ax.set(xlabel='', ylabel='Firing Rate of pNK1 Neurons (spk/s)')
# ax.set_ylim([-5,100])
# ax.set_xticklabels(labels=["Control","NK1R-","GABAR-\nGlyR-","GABAR-\nGlyR-\nNK1R-","Control","NK1R-","GABAR-\nGlyR-","GABAR-\nGlyR-\nNK1R-"])
# ax.legend_.remove()

# Plot Figure 11A&B:
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

# Plotting Figure X (GA):
# Boxplots of Firing Rates:
# fig, ax = plt.subplots(1, sharex=False, figsize=(11.6*cm, 7*cm), dpi=1200)
# my_pal2 = {'Exp':'#808080','Cand0':'#FFFFFF','Cand1':'#D3D3D3','Cand2':'#D3D3D3','Cand3':'#D3D3D3','Cand4':'#D3D3D3','Cand5':'#D3D3D3','Cand6':'#D3D3D3','Cand7':'#D3D3D3','Cand8':'#D3D3D3','Cand9':'#D3D3D3'} 
# #my_pal2 = {'Exp':'#555555','Cand0':'#7DAB55','Cand1':'#B1CE95','Cand2':'#4273AF','Cand3':'#A3C0E3','Cand4':'#808080','Cand5':'#BFBFC0','Cand6':'#D64546','Cand7':'#EE8079','Cand8':'#F5C243','Cand9':'#FBE7A2'} 
# ax = sns.boxplot(x="Force", y="Firing Rate",hue="Condition", data=DataMatrix, color='w',palette=my_pal2, showfliers = False)
# #ax = sns.stripplot(x="Force", y="Firing Rate",hue="Condition", data=DataMatrix,palette=my_pal2,size=5,jitter=False,edgecolor="black",linewidth=0.5,dodge=True)
# ax.set(xlabel='', ylabel='Firing Rate of pNK1 Neurons (spk/s)')
# ax.set_ylim([-2,50])
# ax.set_xticklabels(labels=["50 mN","100 mN","200 mN"])
# adjust_box_widths(fig, 0.8)
# ax.legend_.remove()
# Violin Plot of Fitness:
# fig, ax = plt.subplots(1, sharex=False, figsize=(5*cm, 7*cm), dpi=1200)
# my_pal2 = {'Cand0':'#FFFFFF','Cand1':'#D3D3D3','Cand2':'#D3D3D3','Cand3':'#D3D3D3','Cand4':'#D3D3D3','Cand5':'#D3D3D3','Cand6':'#D3D3D3','Cand7':'#D3D3D3','Cand8':'#D3D3D3','Cand9':'#D3D3D3'} 
# ax = sns.violinplot(y="Fitness", data=DataMatrix, dodge=True, inner="box", color="#D3D3D3",linewidth=0.5,width=0.3,saturation=1)
# ax = sns.stripplot(y="Fitness", data=DataMatrix, dodge=False, color="#D3D3D3",size=4, jitter=False,edgecolor="black",linewidth=0.5)
# ax.collections[0].set_edgecolor('black')
# ax.set(xlabel='', ylabel='Fitness')
# ax.set_ylim([0,2])

# TESTING GA SOLUTIONS (VALIDATION)
# fig, ax = plt.subplots(1, sharex=False, figsize=(5*cm, 5*cm), dpi=1200)  # fig 5
# my_pal = {"Control":"w","Disinhibition":"#595959"} # for figure 5
# my_pal2 = {"Control":"w","Disinhibition":"#595959"} # for figure 5
# # plot line at median
# x_coordinates = [-0.5, 8.5]
# y_coordinates = [30, 30]
# ax = plt.plot(x_coordinates, y_coordinates,linestyle='dashed',linewidth=1)
# ax = sns.boxplot(x="Mechanical Force", y="Firing Rate", hue='Type', data=DataMatrix, palette=my_pal,dodge=True, showfliers = False,linewidth=0.5) # for figure 3
# ax = sns.stripplot(x="Mechanical Force", y="Firing Rate", hue='Type',data=DataMatrix, palette=my_pal2,edgecolor="black",jitter=False,dodge=True,size=4,linewidth=0.5)
# ax.set_yticks([0,50,100,150,200,250,300,350,400])
# ax.set_xticklabels(labels=["10","25","200"])
# ax.set(xlabel='Mechanical Force (mN)', ylabel='Firing Rate of pNK1 Neurons (spk/s)')
# # #ax.legend_.set_title(None)
# ax.set_ylim([-5,400])
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
fig.savefig('Figure9A-New.svg', format='svg', dpi=1200)
fig.savefig('Figure9A-New.png', format='png', dpi=1200)

# fig.savefig('Cand10-Dis.svg', format='svg', dpi=1200)
# fig.savefig('Cand10-Dis.png', format='png', dpi=1200)