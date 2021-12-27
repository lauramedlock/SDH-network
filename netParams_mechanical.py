'''Network Parameters script for SDH Network Model 
created by K. Sekiguchi (15Aug20)
updated by L. Medlock (8Apr21 onwards)
'''

from netpyne import specs, sim
from neuron import h
import numpy as np
import cells
import json
# from cfg_mechanical import cfg

try: 
    from __main__ import cfg
except:
    from cfg_mechanical import cfg

netParams = specs.NetParams()

#------------------------------------------------------------------------------
# Population
#------------------------------------------------------------------------------
'''
## INPUT FROM AFFERENT FIBERS WITH RANDOMIZATION FACTOR ###
rate_SAI, t = rate_SAI()
rate_SAII, t = rate_SAII()
rate_Ad, t = rate_Ad()
rate_C, t = rate_C()

spkt_SAI, spkt_SAII, spkt_Ad, spkt_C = [], [], [], []

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

with open('spkt_SAI_%s.json' %(cfg.freq), 'w') as SAI: json.dump(spkt_SAI, SAI)
with open('spkt_SAII_%s.json' %(cfg.freq), 'w') as SAII: json.dump(spkt_SAII, SAII)
with open('spkt_Ad_%s.json' %(cfg.freq), 'w') as Ad: json.dump(spkt_Ad, Ad)
with open('spkt_C_%s.json' %(cfg.freq), 'w') as  C: json.dump(spkt_C, C)
'''

### FIXED INPUT FROM AFFERENT FIBERS (SAME SPIKE TRAINS PER RUN) ###
with open('spkt_SAI_%s.json' %(cfg.freq), 'rb') as spkt_SAI: spkt_SAI = json.load(spkt_SAI)
with open('spkt_SAII_%s.json' %(cfg.freq), 'rb') as spkt_SAII: spkt_SAII = json.load(spkt_SAII)
with open('spkt_Ad_%s.json' %(cfg.freq), 'rb') as spkt_Ad: spkt_Ad = json.load(spkt_Ad)
with open('spkt_C_%s.json' %(cfg.freq), 'rb') as spkt_C: spkt_C = json.load(spkt_C)

## PRIMARY AFFERENTS -- TIME-VARYING INPUT SPIKE TRAINS IMPORTED AS VECTSTIM
netParams.popParams['Ab_SAI'] = {'cellModel': 'VecStim', 'numCells': 10, 'spkTimes': spkt_SAI}  # 0-9 input from Ab_slow adapting type I
netParams.popParams['Ab_SAII'] = {'cellModel': 'VecStim', 'numCells': 10, 'spkTimes': spkt_SAII}  # 10-19 input from Ab_slow adapting type II
netParams.popParams['Ad'] = {'cellModel': 'VecStim', 'numCells': 20, 'spkTimes': spkt_Ad}  # 20-39 input from Adelta
netParams.popParams['C_PEP'] = {'cellModel': 'VecStim', 'numCells': 80, 'spkTimes': spkt_C}  # 40 - 119 input from peptidergic C fibers
netParams.popParams['C_NP'] = {'cellModel': 'VecStim', 'numCells': 80, 'spkTimes': spkt_C}  # 120-199 input from non-peptidergic C fibers

## SETTING OF SPINAL NEURONS
cells.PKCRule['conds'] = {'cellType': 'PKC'}
cells.INcellRule['conds'] = {'cellType': 'IN'}
cells.EXdelayedRule['conds'] = {'cellType': 'EXdl'}
cells.CRRule['conds'] = {'cellType': 'CR'}
cells.SOMRule['conds'] = {'cellType': 'SOM'}
cells.EXinitialRule['conds'] = {'cellType': 'EXib'}
cells.PROcellRule['conds'] = {'cellType': 'PRO'}

cells.PROcellRule['secs']['soma']['threshold'] = 0

netParams.cellParams['PKC'] = cells.PKCRule
netParams.cellParams['VGLUT3Rule'] = cells.EXdelayedRule
netParams.cellParams['PVRule'] = cells.INcellRule
netParams.cellParams['DORRule'] = cells.EXdelayedRule
netParams.cellParams['TrCRule'] = cells.EXinitialRule
netParams.cellParams['DYNRule'] = cells.INcellRule
netParams.cellParams['SOMRule'] = cells.SOMRule
netParams.cellParams['CRRule'] = cells.CRRule
netParams.cellParams['ISLETRule'] = cells.INcellRule
netParams.cellParams['NK1Rule'] = cells.PROcellRule

## SETTING POPULATION OF SPINAL NEURONS
netParams.popParams['PKC' ] = {'cellType': 'PKC', 'numCells': 0} # 30 # PKCg+ neurons (excitatory) 200-229 
netParams.popParams['VGLUT3'] = {'cellType': 'EXdl', 'numCells': 4} # 4 VGLUT3+ neurons (excitatory)  230-233
netParams.popParams['PV'] = {'cellType': 'IN', 'numCells': 0} # 15 # PV+ neurons (inhibitory)      234-248
netParams.popParams['DOR' ] = {'cellType': 'EXdl', 'numCells': 0} # 30 # DOR+ neurons (excitatory)  249-278
netParams.popParams['TrC'] = {'cellType': 'EXib', 'numCells': 10} # Transient Central neurons (excitatory) 279-288
netParams.popParams['DYN'] = {'cellType': 'IN', 'numCells': 60} # 60 # Central/DYN+ neurons (inhibitory) 289-348
netParams.popParams['SOM'] = {'cellType': 'SOM', 'numCells': 0} # 15 # SOM+ neurons (excitatory) 349-363
netParams.popParams['CR'] = {'cellType': 'CR', 'numCells': 20} # 20 CR+ neurons (excitatory) 364-383
netParams.popParams['ISLET'] = {'cellType': 'IN', 'numCells': 15} # Islet-type neurons (inhibitory) 384-398
netParams.popParams['NK1'] = {'cellType': 'PRO', 'numCells': 10} # NK1+ neurons (projection) 399-408

###################################################################################################################################
#   Synaptic Mechanisms
###################################################################################################################################
netParams.defaultThreshold = -30

netParams.synMechParams['AMPA']  = {'mod': 'AMPA_DynSyn'   , 'tau_rise': 0.1, 'tau_decay': 5            }
netParams.synMechParams['NMDA']  = {'mod': 'NMDA_DynSyn'   , 'tau_rise': 2  , 'tau_decay': 100          }
netParams.synMechParams['NK13']  = {'mod': 'NK1_DynSyn'    , 'tau_rise': 100, 'tau_decay': 1000         }
netParams.synMechParams['NK23']  = {'mod': 'NK1_DynSyn'    , 'tau_rise': 200, 'tau_decay': 3000         }
netParams.synMechParams['GABA']  = {'mod': 'GABAa_DynSyn'  , 'tau_rise': 0.1, 'tau_decay': 20, 'e': -70 }  # GABA for Excitatory Neur
netParams.synMechParams['GABA2'] = {'mod': 'GABAa_DynSyn'  , 'tau_rise': 0.1, 'tau_decay': 20, 'e': -70 }  # GABA for Inhibitory Neur
netParams.synMechParams['GLY']   = {'mod': 'Glycine_DynSyn', 'tau_rise': 0.1, 'tau_decay': 10, 'e': -70 }  # Gly for Excitatory Neur
netParams.synMechParams['GLY2']  = {'mod': 'Glycine_DynSyn', 'tau_rise': 0.1, 'tau_decay': 10, 'e': -70 }  # Gly for Inhibitory Neur

###################################################################################################################################
#   Connect the spinal cord stimulation/natural input
###################################################################################################################################
# from Ab_SAI to interneurons
netParams.connParams['Ab_SAI_AMPA->PKC'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'Ab_SAI'}, 
    'postConds': {'popLabel': 'PKC'},  
    'weight': cfg.Ab_EX_AMPA,           
    'sec': 'dend',
    'probability': 0.2,
    'delay': 1.0,
    'loc': 0.5,
    'synMech': 'AMPA'} 

netParams.connParams['Ab_SAI_NMDA->PKC'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'Ab_SAI'}, 
    'postConds': {'popLabel': 'PKC'},  
    'weight': cfg.Ab_EX_NMDA,           
    'sec': 'dend',
    'probability': 0.2,
    'delay': 1.0,
    'loc': 0.5,
    'synMech': 'NMDA'} 

netParams.connParams['Ab_SAI_AMPA->VGLUT3'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'Ab_SAI'}, 
    'postConds': {'popLabel': 'VGLUT3'},  
    'weight': cfg.Ab_EX_AMPA,           
    'sec': 'dend',
    'probability': 0.2,
    'delay': 1.0,
    'loc': 0.5,
    'synMech': 'AMPA'} 

netParams.connParams['Ab_SAI_NMDA->VGLUT3'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'Ab_SAI'}, 
    'postConds': {'popLabel': 'VGLUT3'},  
    'weight': cfg.Ab_EX_NMDA,           
    'sec': 'dend',
    'probability': 0.2,
    'delay': 1.0,
    'loc': 0.5,
    'synMech': 'NMDA'} 

netParams.connParams['Ab_SAI_AMPA->PV'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'Ab_SAI'}, 
    'postConds': {'popLabel': 'PV'},  
    'weight': cfg.Ab_IN_AMPA,           
    'sec': 'dend',
    'probability': 0.2,
    'delay': 1.0,
    'loc': 0.5,
    'synMech': 'AMPA'} 

netParams.connParams['Ab_SAI_NMDA->PV'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'Ab_SAI'}, 
    'postConds': {'popLabel': 'PV'},  
    'weight': cfg.Ab_IN_NMDA,           
    'sec': 'dend',
    'probability': 0.2,
    'delay': 1.0,
    'loc': 0.5,
    'synMech': 'NMDA'} 

netParams.connParams['Ab_SAI_AMPA->DYN'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'Ab_SAI'}, 
    'postConds': {'popLabel': 'DYN'},  
    'weight': cfg.Ab_IN_AMPA,           
    'sec': 'dend',
    'probability': 0.2,
    'delay': 1.0,
    'loc': 0.5,
    'synMech': 'AMPA'} 

# from Ab_SAII to interneurons
netParams.connParams['Ab_SAII_AMPA->PKC'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'Ab_SAII'}, 
    'postConds': {'popLabel': 'PKC'},  
    'weight': cfg.Ab_EX_AMPA,           
    'sec': 'dend',
    'probability': 0.2,
    'delay': 1.0,
    'loc': 0.5,
    'synMech': 'AMPA'} 

netParams.connParams['Ab_SAII_NMDA->PKC'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'Ab_SAII'}, 
    'postConds': {'popLabel': 'PKC'},  
    'weight': cfg.Ab_EX_NMDA,           
    'sec': 'dend',
    'probability': 0.2,
    'delay': 1.0,
    'loc': 0.5,
    'synMech': 'NMDA'} 

netParams.connParams['Ab_SAII_AMPA->VGLUT3'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'Ab_SAII'}, 
    'postConds': {'popLabel': 'VGLUT3'},  
    'weight': cfg.Ab_EX_AMPA,           
    'sec': 'dend',
    'probability': 0.2,
    'delay': 1.0,
    'loc': 0.5,
    'synMech': 'AMPA'} 

netParams.connParams['Ab_SAII_NMDA->VGLUT3'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'Ab_SAII'}, 
    'postConds': {'popLabel': 'VGLUT3'},  
    'weight': cfg.Ab_EX_NMDA,           
    'sec': 'dend',
    'probability': 0.2,
    'delay': 1.0,
    'loc': 0.5,
    'synMech': 'NMDA'} 

netParams.connParams['Ab_SAII_AMPA->PV'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'Ab_SAII'}, 
    'postConds': {'popLabel': 'PV'},  
    'weight': cfg.Ab_IN_AMPA,           
    'sec': 'dend',
    'probability': 0.2,
    'delay': 1.0,
    'loc': 0.5,
    'synMech': 'AMPA'} 

netParams.connParams['Ab_SAII_NMDA->PV'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'Ab_SAII'}, 
    'postConds': {'popLabel': 'PV'},  
    'weight': cfg.Ab_IN_NMDA,           
    'sec': 'dend',
    'probability': 0.2,
    'delay': 1.0,
    'loc': 0.5,
    'synMech': 'NMDA'} 

netParams.connParams['Ab_SAII_AMPA->DYN'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'Ab_SAII'}, 
    'postConds': {'popLabel': 'DYN'},  
    'weight': cfg.Ab_IN_AMPA,           
    'sec': 'dend',
    'probability': 0.2,
    'delay': 1.0,
    'loc': 0.5,
    'synMech': 'AMPA'} 

# from Ad to interneurons
netParams.connParams['Ad_AMPA->DOR'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'Ad'}, 
    'postConds': {'popLabel': 'DOR'},  
    'weight': cfg.Ad_AMPA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 5.0,
    'loc': 0.50,
    'synMech': 'AMPA'}

netParams.connParams['Ad_NMDA->DOR'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'Ad'}, 
    'postConds': {'popLabel': 'DOR'},  
    'weight': cfg.Ad_NMDA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 5.0,
    'loc': 0.50,
    'synMech': 'NMDA'}

netParams.connParams['Ad_AMPA->SOM'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'Ad'}, 
    'postConds': {'popLabel': 'SOM'},  
    'weight': cfg.Ad_AMPA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 5.0,
    'loc': 0.50,
    'synMech': 'AMPA'}

netParams.connParams['Ad_NMDA->SOM'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'Ad'}, 
    'postConds': {'popLabel': 'SOM'},  
    'weight': cfg.Ad_NMDA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 5.0,
    'loc': 0.50,
    'synMech': 'NMDA'}

netParams.connParams['Ad_AMPA->CR'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'Ad'}, 
    'postConds': {'popLabel': 'CR'},  
    'weight': cfg.Ad_AMPA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 5.0,
    'loc': 0.50,
    'synMech': 'AMPA'}

netParams.connParams['Ad_NMDA->CR'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'Ad'}, 
    'postConds': {'popLabel': 'CR'},  
    'weight': cfg.Ad_NMDA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 5.0,
    'loc': 0.50,
    'synMech': 'NMDA'}

# from peptidergic C to interneurons
netParams.connParams['C_PEP_AMPA->TrC'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'C_PEP'}, 
    'postConds': {'popLabel': 'TrC'},  
    'weight': cfg.C_TrC_AMPA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 10.0,
    'loc': 0.5,
    'synMech': 'AMPA'}

netParams.connParams['C_PEP_AMPA->SOM'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'C_PEP'}, 
    'postConds': {'popLabel': 'SOM'},  
    'weight': cfg.C_EX_AMPA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 10.0,
    'loc': 0.5,
    'synMech': 'AMPA'}

netParams.connParams['C_PEP_NMDA->SOM'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'C_PEP'}, 
    'postConds': {'popLabel': 'SOM'},  
    'weight': cfg.C_EX_NMDA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 10.0,
    'loc': 0.5,
    'synMech': 'NMDA'}

netParams.connParams['C_PEP_AMPA->CR'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'C_PEP'}, 
    'postConds': {'popLabel': 'CR'},  
    'weight': cfg.C_EX_AMPA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 10.0,
    'loc': 0.5,
    'synMech': 'AMPA'}

netParams.connParams['C_PEP_NMDA->CR'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'C_PEP'}, 
    'postConds': {'popLabel': 'CR'},  
    'weight': cfg.C_EX_NMDA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 10.0,
    'loc': 0.5,
    'synMech': 'NMDA'}

netParams.connParams['C_PEP_AMPA->DYN'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'C_PEP'}, 
    'postConds': {'popLabel': 'DYN'},  
    'weight': cfg.C_DYN_AMPA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 10.0,
    'loc': 0.5,
    'synMech': 'AMPA'}

netParams.connParams['C_PEP_AMPA->ISLET'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'C_PEP'}, 
    'postConds': {'popLabel': 'ISLET'},  
    'weight': cfg.C_ISLET_AMPA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 10.0,
    'loc': 0.5,
    'synMech': 'AMPA'}

netParams.connParams['C_PEP_AMPA->NK1'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'C_PEP'}, 
    'postConds': {'popLabel': 'NK1'},  
    'weight': cfg.C_NK1_AMPA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 10.0,
    'loc': 0.5,
    'synMech': 'AMPA'}

netParams.connParams['C_PEP_NMDA->NK1'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'C_PEP'}, 
    'postConds': {'popLabel': 'NK1'},  
    'weight': cfg.C_NK1_NMDA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 10.0,
    'loc': 0.5,
    'synMech': 'NMDA'}

netParams.connParams['C_PEP_NK1->NK1'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'C_PEP'}, 
    'postConds': {'popLabel': 'NK1'},  
    'weight': cfg.C_NK1_NK1,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 10.0,
    'loc': 0.5,
    'synMech': 'NK13'}

# from non-peptidergic C to interneurons
netParams.connParams['C_NP_AMPA->TrC'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'C_NP'}, 
    'postConds': {'popLabel': 'TrC'},  
    'weight': cfg.C_TrC_AMPA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 10.0,
    'loc': 0.5,
    'synMech': 'AMPA'}

netParams.connParams['C_NP_AMPA->SOM'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'C_NP'}, 
    'postConds': {'popLabel': 'SOM'},  
    'weight': cfg.C_EX_AMPA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 10.0,
    'loc': 0.5,
    'synMech': 'AMPA'}

netParams.connParams['C_NP_NMDA->SOM'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'C_NP'}, 
    'postConds': {'popLabel': 'SOM'},  
    'weight': cfg.C_EX_NMDA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 10.0,
    'loc': 0.5,
    'synMech': 'NMDA'}

netParams.connParams['C_NP_AMPA->CR'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'C_NP'}, 
    'postConds': {'popLabel': 'CR'},  
    'weight': cfg.C_EX_AMPA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 10.0,
    'loc': 0.5,
    'synMech': 'AMPA'}

netParams.connParams['C_NP_NMDA->CR'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'C_NP'}, 
    'postConds': {'popLabel': 'CR'},  
    'weight': cfg.C_EX_NMDA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 10.0,
    'loc': 0.5,
    'synMech': 'NMDA'}

netParams.connParams['C_NP_AMPA->DYN'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'C_NP'}, 
    'postConds': {'popLabel': 'DYN'},  
    'weight': cfg.C_DYN_AMPA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 10.0,
    'loc': 0.5,
    'synMech': 'AMPA'}

netParams.connParams['C_NP_AMPA->ISLET'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'C_NP'}, 
    'postConds': {'popLabel': 'ISLET'},  
    'weight': cfg.C_ISLET_AMPA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 10.0,
    'loc': 0.5,
    'synMech': 'AMPA'}

###################################################################################################################################
#   Connect spinal neurons (inh>ex, ex>ex, ex/inh>projection)
###################################################################################################################################
# TO PKC NEURONS
netParams.connParams['VGLUT3_AMPA->PKC'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'VGLUT3'}, 
    'postConds': {'popLabel':'PKC'},  
    'weight': cfg.VGLUT3_PKC_AMPA,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'AMPA'}

netParams.connParams['VGLUT3_NMDA->PKC'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'VGLUT3'}, 
    'postConds': {'popLabel':'PKC'},  
    'weight': cfg.VGLUT3_PKC_NMDA,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'NMDA'}

netParams.connParams['PV_GABA->PKC'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'PV'}, 
    'postConds': {'popLabel':'PKC'},  
    'weight': cfg.PV_GABA,          
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'GABA'}

netParams.connParams['PV_GLY->PKC'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'PV'}, 
    'postConds': {'popLabel':'PKC'},  
    'weight': cfg.PV_GLY,        
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'GLY'}

# TO DOR NEURONS
netParams.connParams['PV_GABA->DOR'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'PV'}, 
    'postConds': {'popLabel':'DOR'},  
    'weight': cfg.PV_GABA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'GABA'}

netParams.connParams['PV_GLY->DOR'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'PV'}, 
    'postConds': {'popLabel':'DOR'},  
    'weight': cfg.PV_GLY,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'GLY'}

netParams.connParams['VGLUT3_AMPA->DOR'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'VGLUT3'}, 
    'postConds': {'popLabel':'DOR'},  
    'weight': cfg.VGLUT3_PKC_AMPA,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'AMPA'}

netParams.connParams['VGLUT3_NMDA->DOR'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'VGLUT3'}, 
    'postConds': {'popLabel':'DOR'},  
    'weight': cfg.VGLUT3_PKC_NMDA,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'NMDA'}

# TO TrC NEURONS
netParams.connParams['PKC_AMPA->TrC'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'PKC'}, 
    'postConds': {'popLabel':'TrC'},  
    'weight': cfg.PKC_AMPA,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'AMPA'}

netParams.connParams['ISLET_GABA->TrC'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'ISLET'}, 
    'postConds': {'popLabel':'TrC'},  
    'weight': cfg.ISLET_GABA,       
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'GABA'}  # inhibitory --> excitatory (GABA)

# TO ISLET NEURONS
netParams.connParams['DYN_GABA->ISLET'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'DYN'}, 
    'postConds': {'popLabel':'ISLET'},  
    'weight': cfg.DYN_ISLET_GABA,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'GABA2'}   # inhibitory --> inhibitory (GABA2)

# TO DYN NEURONS
netParams.connParams['ISLET_GABA->DYN'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'ISLET'}, 
    'postConds': {'popLabel':'DYN'},  
    'weight': cfg.ISLET_GABA,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'GABA2'}  # inhibitory --> inhibitory (GABA2)

# TO SOM NEURONS
netParams.connParams['DYN_GABA->SOM'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'DYN'}, 
    'postConds': {'popLabel':'SOM'},  
    'weight': cfg.DYN_EX_GABA,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'GABA'}

netParams.connParams['DYN_GLY->SOM'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'DYN'}, 
    'postConds': {'popLabel':'SOM'},  
    'weight': cfg.DYN_EX_GLY,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'GLY'}

netParams.connParams['TrC_AMPA->SOM'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'TrC'}, 
    'postConds': {'popLabel':'SOM'},  
    'weight': cfg.TrC_AMPA,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'AMPA'}

netParams.connParams['TrC_NMDA->SOM'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'TrC'}, 
    'postConds': {'popLabel':'SOM'},  
    'weight': cfg.TrC_NMDA,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'NMDA'}

netParams.connParams['PKC_AMPA->SOM'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'PKC'}, 
    'postConds': {'popLabel':'SOM'},  
    'weight': cfg.PKC_AMPA,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'AMPA'}

netParams.connParams['PKC_NMDA->SOM'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'PKC'}, 
    'postConds': {'popLabel':'SOM'},  
    'weight': cfg.PKC_NMDA,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'NMDA'}

netParams.connParams['VGLUT3_AMPA->SOM'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'VGLUT3'}, 
    'postConds': {'popLabel':'SOM'},  
    'weight': cfg.VGLUT3_SOM_AMPA,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'AMPA'}

netParams.connParams['VGLUT3_NMDA->SOM'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'VGLUT3'}, 
    'postConds': {'popLabel':'SOM'},  
    'weight': cfg.VGLUT3_SOM_NMDA,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'NMDA'}

netParams.connParams['DOR_AMPA->SOM'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'DOR'}, 
    'postConds': {'popLabel':'SOM'},  
    'weight': cfg.DOR_AMPA,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'AMPA'}

netParams.connParams['DOR_NMDA->SOM'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'DOR'}, 
    'postConds': {'popLabel':'SOM'},  
    'weight': cfg.DOR_NMDA,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'NMDA'}

# TO CR NEURONS
netParams.connParams['DYN_GABA->CR'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'DYN'}, 
    'postConds': {'popLabel':'CR'},  
    'weight': cfg.DYN_EX_GABA,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'GABA'}

netParams.connParams['DYN_GLY->CR'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'DYN'}, 
    'postConds': {'popLabel':'CR'},  
    'weight': cfg.DYN_EX_GLY,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'GLY'}

netParams.connParams['TrC_AMPA->CR'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'TrC'}, 
    'postConds': {'popLabel':'CR'},  
    'weight': cfg.TrC_AMPA,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'AMPA'}

netParams.connParams['TrC_NMDA->CR'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'TrC'}, 
    'postConds': {'popLabel':'CR'},  
    'weight': cfg.TrC_NMDA,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'NMDA'}

netParams.connParams['PKC_AMPA->CR'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'PKC'}, 
    'postConds': {'popLabel':'CR'},  
    'weight': cfg.PKC_AMPA,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'AMPA'}

netParams.connParams['PKC_NMDA->CR'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'PKC'}, 
    'postConds': {'popLabel':'CR'},  
    'weight': cfg.PKC_NMDA,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'NMDA'}

netParams.connParams['DOR_AMPA->CR'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'DOR'}, 
    'postConds': {'popLabel':'CR'},  
    'weight': cfg.DOR_AMPA,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'AMPA'}

netParams.connParams['DOR_NMDA->CR'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'DOR'}, 
    'postConds': {'popLabel':'CR'},  
    'weight': cfg.DOR_NMDA,           
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'NMDA'}

# TO NK1 NEURONS
netParams.connParams['SOM_AMPA->NK1'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'SOM'}, 
    'postConds': {'popLabel': 'NK1'},  
    'weight': cfg.EX_NK1_AMPA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'AMPA'}

netParams.connParams['SOM_NMDA->NK1'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'SOM'}, 
    'postConds': {'popLabel': 'NK1'},  
    'weight': cfg.EX_NK1_NMDA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'NMDA'}

netParams.connParams['SOM_NK1->NK1'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'SOM'}, 
    'postConds': {'popLabel': 'NK1'},  
    'weight': cfg.EX_NK1_NK1,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'NK13'}

netParams.connParams['CR_AMPA->NK1'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'CR'}, 
    'postConds': {'popLabel': 'NK1'},  
    'weight': cfg.EX_NK1_AMPA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'AMPA'}

netParams.connParams['CR_NMDA->NK1'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'CR'}, 
    'postConds': {'popLabel': 'NK1'},  
    'weight': cfg.EX_NK1_NMDA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'NMDA'}

netParams.connParams['CR_NK1->NK1'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'CR'}, 
    'postConds': {'popLabel': 'NK1'},  
    'weight': cfg.EX_NK1_NK1,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'NK13'}

netParams.connParams['DYN_GABA->NK1'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'DYN'}, 
    'postConds': {'popLabel': 'NK1'},  
    'weight': cfg.DYN_NK1_GABA,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'GABA'}

netParams.connParams['DYN_GLY->NK1'] = {
    'oneSynPerNetcon': True,
    'preConds': {'popLabel': 'DYN'}, 
    'postConds': {'popLabel': 'NK1'},  
    'weight': cfg.DYN_NK1_GLY,
    'probability': 0.2,
    'sec': 'dend',
    'delay': 0.5, 
    'loc': 0.5,
    'synMech': 'GLY'}