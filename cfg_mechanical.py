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
cfg.stim_ratios = 0.001 # 0mN to 25mN -> 0.001, 50mN -> 0.125, 100mN -> 0.25, 200mN -> 0.5, 400mN -> 1.0, 800mN --> 2.0
# STIMULATION RATIO OF AB FIBERS ###
cfg.AB_ratio = 0.4    # 0mN -> 0.001, 5mN->0.1, 10mN->0.2, 15mN->0.3, 20mN->0.4, 25mN->0.5, 30mN->0.6, 50mN->1.0, 100mN->1.0, 200mN -> 1.0, 400mN -> 1.0, 800mN --> 1.0

cfg.freq = '25mN' #Change freq to match the stimulus given above

### SYNAPTIC WEIGHTS FOR FINAL MODEL ###
# cfg.Ab_EX_AMPA = 0.0221559
# cfg.Ab_EX_NMDA = 0.015
# cfg.Ab_IN_AMPA = 0.00208312
# cfg.Ab_IN_NMDA = 0.0098189
# cfg.Ad_AMPA = 1.50e-05                
# cfg.Ad_NMDA = 1.50e-05                
# cfg.C_EX_AMPA = 0.00067115     
# cfg.C_EX_NMDA = 0.000407345    
# cfg.C_TrC_AMPA = 0.164705             
# cfg.C_DYN_AMPA = 0.184135             
# cfg.C_ISLET_AMPA = 0.123535             
# cfg.C_NK1_AMPA = 0.00009       
# cfg.C_NK1_NMDA = 8.7447e-05    
# cfg.C_NK1_NK1 = 3.2414e-08       
# cfg.VGLUT3_PKC_AMPA = 0.16629
# cfg.VGLUT3_PKC_NMDA = 0.15549
# cfg.PV_GABA = 0.29416             #*0.6  #alt tuning (7C)
# cfg.PV_GLY =  0.011521            #*0.6  #alt tuning (7C)
# cfg.DYN_ISLET_GABA = 0.36182   
# cfg.ISLET_GABA = 0.34293     
# cfg.DYN_EX_GABA = 4.50e-05       #*25  #alt tuning (7C)
# cfg.DYN_EX_GLY = 4.50e-05        #*25  #alt tuning (7C)
# cfg.PKC_AMPA = 0.0021
# cfg.PKC_NMDA = 0.00315
# cfg.TrC_AMPA = 0.00225             
# cfg.TrC_NMDA = 0.003              
# cfg.VGLUT3_SOM_AMPA = 0.00006
# cfg.VGLUT3_SOM_NMDA = 0.00006
# cfg.DOR_AMPA = 0.002250          
# cfg.DOR_NMDA = 0.002250           
# cfg.EX_NK1_AMPA = 8.82981e-06          
# cfg.EX_NK1_NMDA = 2.6699e-05
# cfg.EX_NK1_NK1 = 9.2715e-07      
# cfg.DYN_NK1_GABA = 6.3720e-06   
# cfg.DYN_NK1_GLY = 2.3608e-06       

## TESTING GA RERUNS -- ORDER OF WEIGHTS FROM EXCEL ##
cfg.Ab_EX_AMPA =             5.94E-07
cfg.Ab_EX_NMDA =             0.001854194
cfg.Ab_IN_AMPA =             0.002458819
cfg.Ab_IN_NMDA =             0.406985708
cfg.Ad_AMPA =                0.203200929 *0
cfg.Ad_NMDA =                0.023468298 *0
cfg.C_EX_AMPA =              0.30940143  *0
cfg.C_EX_NMDA =              0.123749217 *0
cfg.C_TrC_AMPA =             0.024647308 *0
cfg.C_DYN_AMPA =             0.232290171 *0
cfg.C_ISLET_AMPA =           0.499877745 *0
cfg.C_NK1_AMPA =             0.066640917 *0
cfg.C_NK1_NMDA =             0.162674037 *0
cfg.C_NK1_NK1 =              1.20E-07    *0
cfg.VGLUT3_PKC_AMPA =        0.157810762
cfg.VGLUT3_PKC_NMDA =        0.488686215
cfg.PV_GABA =                0.270994481 *0
cfg.PV_GLY =                 0.462461078 *0
cfg.DYN_ISLET_GABA =         0.358243694 *0
cfg.ISLET_GABA =             0.499795634 *0
cfg.DYN_EX_GABA =            0.489710889 *0
cfg.DYN_EX_GLY =             0.010633683 *0
cfg.PKC_AMPA =               0.253529138
cfg.PKC_NMDA =               0.25613928
cfg.TrC_AMPA =               0.008708131
cfg.TrC_NMDA =               0.002245108
cfg.VGLUT3_SOM_AMPA =        0.374821997
cfg.VGLUT3_SOM_NMDA =        0.131795081
cfg.DOR_AMPA =               3.81E-05
cfg.DOR_NMDA =               0.162578679
cfg.EX_NK1_AMPA =            0.246032084
cfg.EX_NK1_NMDA =            0.475734091
cfg.EX_NK1_NK1 =             1.11E-08
cfg.DYN_NK1_GABA =           0.052827152 *0
cfg.DYN_NK1_GLY =            0.499162858 *0


# testing Ab-->eSST
# cfg.Ab_SOM_AMPA = 0.09 
# cfg.Ab_SOM_NMDA = 0.09  

cfg.recordTraces['vs'] = {'sec':'soma', 'loc':0.5,'var':'v'}

# SAVING
cfg.simLabel = '25mN-IRB-Cblock-CandI'
cfg.saveFolder = 'data_batch'
cfg.saveDataInclude = ['simData', 'simConfig', 'netParams']
cfg.saveMat = False
cfg.saveJson = True

# ANALYSIS AND PLOTTING
cells = [x for x in range(400, 410, 1)]
cfg.analysis['plotRaster'] = {'include': ['all'], 'timeRange': [0, cfg.duration], 'saveFig': True, 'showFig': False} #'raster.png'
# cfg.analysis['plotSpikeHist'] = {'include': ['eachPop'], 'timeRange': [0,cfg.duration], 'spikeHistBin': 5, 'saveFig': True, 'showFig': False}
cfg.analysis['plotSpikeStats'] = {'include': ['eachPop'], 'timeRange': [0,cfg.duration], 'saveFig': True, 'showFig': False}
#cfg.analysis['plotConn'] = {'includePre': ['all'], 'includePost': ['all'], 'feature': 'weight', 'saveFig': True, 'showFig': False, 'logPlot': True}
cfg.analysis['plotTraces'] = {'include': [399,400,401,402,403,404,405,406,407,408,409],'oneFigPer':'trace','timeRange': [0, cfg.duration], 'saveFig': True, 'showFig': False}
# cfg.analysis['plot2Dnet'] = False 

# use for GA simulation
cfg.verbose = True
cfg.printPopAvgRates = [0, 5000]
cfg.dt = 0.025

