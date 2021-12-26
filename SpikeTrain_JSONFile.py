"""
Created on Fri May 14 09:46:44 2021

Use this code to generate new JSON files for primary afferent input
Need to change firing rate scaling in cfg_mechanical.py file first

@author: lauramed
"""
#%% SPIKE TRAIN GENERATION

from spkt_gen import *
import json

## INPUT FREQUENCY FROM AFFERENT FIBERS WITH RANDOM FACTOR ###
rate_SAI, t = rate_SAI()
rate_SAII, t = rate_SAII()
rate_Ad, t = rate_Ad()
rate_C, t = rate_C()

spkt_SAI, spkt_SAII, spkt_Ad, spkt_C = [], [], [], []

#%% Run this code after the first part ^
for i in range(10):
    spkt_SAI_ = inh_poisson_generator(rate_SAI, t, 5000, seed=123)
    spkt_SAII_ = inh_poisson_generator(rate_SAII, t, 5000, seed=123)
    spkt_SAI.append(spkt_SAI_)
    spkt_SAII.append(spkt_SAII_)

for i in range(20):
    spkt_Ad_ = inh_poisson_generator(rate_Ad, t, 5000, seed=123)
    spkt_Ad.append(spkt_Ad_)

for i in range(80):
    spkt_C_ = inh_poisson_generator(rate_C, t, 5000, seed=123)
    spkt_C.append(spkt_C_)

#with open('spkt_SAI_%s.json' %(cfg.freq), 'w') as SAI: json.dump(spkt_SAI, SAI)
#with open('spkt_SAII_%s.json' %(cfg.freq), 'w') as SAII: json.dump(spkt_SAII, SAII)
with open('spkt_Ad_%s-New.json' %(cfg.freq), 'w') as Ad: json.dump(spkt_Ad, Ad)
with open('spkt_C_%s-New.json' %(cfg.freq), 'w') as  C: json.dump(spkt_C, C)
# %%
