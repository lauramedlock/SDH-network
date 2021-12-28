'''Configuration script for SDH Network Model 
created by K. Sekiguchi (15Aug20)
updated by L. Medlock (8Apr21 onwards)
'''

from netpyne import specs
from neuron import h

cfg = specs.SimConfig()  
cfg.hParams = {'celsius': 36, 'v_init': -60 }
cfg.vrest = cfg.hParams['v_init']
cfg.duration = 5000
cfg.recordStep = 0.025

#*--------------------------------*#
#*--- PARAMETERS FOR NETPARAMS ---*#
#*--------------------------------*#
# STIMULATION RATIO OF C AND AD FIBERS ###
cfg.stim_ratios = 0.001 # 0mN -> 0.001, 5mN to 20mN -> 0.001, 25mN -> 0.001 (old: 0.0625), 50mN -> 0.125, 100mN -> 0.25, 200mN -> 0.5, 400mN -> 1.0, 800mN --> 2.0
# STIMULATION RATIO OF AB FIBERS ###
cfg.AB_ratio = 0.4    # 0mN -> 0.001, 5mN->0.1, 10mN->0.2, 15mN->0.3, 20mN->0.4, 25mN->0.5, 50mN->1.0, 100mN->1.0, 200mN -> 1.0, 400mN -> 1.0, 800mN --> 1.0

cfg.freq = '20mN' #Change freq to match the stimulus given above

### SYNAPTIC WEIGHTS FOR FINAL MODEL ###
cfg.Ab_EX_AMPA = 0.0221559
cfg.Ab_EX_NMDA = 0.015
cfg.Ab_IN_AMPA = 0.00208312
cfg.Ab_IN_NMDA = 0.0098189
cfg.Ad_AMPA = 1.50e-05                
cfg.Ad_NMDA = 1.50e-05                
cfg.C_EX_AMPA = 0.00067115
cfg.C_EX_NMDA = 0.000407345
cfg.C_TrC_AMPA = 0.164705             
cfg.C_DYN_AMPA = 0.184135             
cfg.C_ISLET_AMPA = 0.123535             
cfg.C_NK1_AMPA = 0.00009
cfg.C_NK1_NMDA = 8.7447e-05
cfg.C_NK1_NK1 = 3.2414e-08       
cfg.VGLUT3_PKC_AMPA = 0.16629
cfg.VGLUT3_PKC_NMDA = 0.15549
cfg.PV_GABA = 0.29416                *0     #*0.6  #alt tuning (7C)
cfg.PV_GLY =  0.011521               *0     #*0.6  #alt tuning (7C)
cfg.DYN_ISLET_GABA = 0.36182         *0
cfg.ISLET_GABA = 0.34293             *0
cfg.DYN_EX_GABA = 4.50e-05           *0     #*25  #alt tuning (7C)
cfg.DYN_EX_GLY = 4.50e-05            *0     #*25  #alt tuning (7C)
cfg.PKC_AMPA = 0.0021
cfg.PKC_NMDA = 0.00315
cfg.TrC_AMPA = 0.00225             
cfg.TrC_NMDA = 0.003              
cfg.VGLUT3_SOM_AMPA = 0.00006
cfg.VGLUT3_SOM_NMDA = 0.00006
cfg.DOR_AMPA = 0.002250          
cfg.DOR_NMDA = 0.002250           
cfg.EX_NK1_AMPA = 8.82981e-06          
cfg.EX_NK1_NMDA = 2.6699e-05
cfg.EX_NK1_NK1 = 9.2715e-07      
cfg.DYN_NK1_GABA = 6.3720e-06        *0
cfg.DYN_NK1_GLY = 2.3608e-06         *0 

cfg.recordTraces['vs'] = {'sec':'soma', 'loc':0.5,'var':'v'}

# SAVING
cfg.simLabel = '20mN-IRB-110%KA'
cfg.saveFolder = 'data_batch'
cfg.saveDataInclude = ['simData', 'simConfig', 'netParams']
cfg.saveMat = True
cfg.saveJson = True

# ANALYSIS AND PLOTTING
cells = [x for x in range(400, 410, 1)]
cfg.analysis['plotRaster'] = {'include': ['all'], 'timeRange': [0, cfg.duration], 'saveFig': True, 'showFig': False} #'raster.png'
# cfg.analysis['plotSpikeHist'] = {'include': ['eachPop'], 'timeRange': [0,cfg.duration], 'spikeHistBin': 5, 'saveFig': True, 'showFig': False}
# cfg.analysis['plotSpikeStats'] = {'include': ['eachPop'], 'timeRange': [0,cfg.duration], 'saveFig': True, 'showFig': False}
# cfg.analysis['plotConn'] = {'includePre': ['all'], 'includePost': ['all'], 'feature': 'weight', 'saveFig': True, 'showFig': False, 'logPlot': True}
# cfg.analysis['plotTraces'] = {'include': cells, 'timeRange': [0, cfg.duration], 'saveFig': True, 'showFig': False}
# cfg.analysis['plot2Dnet'] = False 

# use for GA simulation
cfg.verbose = True
cfg.printPopAvgRates = [ 0, 5000 ]
cfg.dt = 0.025

