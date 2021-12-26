'''Initialization script for SDH Network Model 
created by K. Sekiguchi (15Aug20)
updated by L. Medlock (8Apr21 onwards)
'''
from netpyne import sim
from neuron import h
import os
					
simConfig, netParams = sim.readCmdLineArgs(simConfigDefault='cfg_mechanical.py', netParamsDefault='netParams_mechanical.py')

# Create network and run simulation
sim.createSimulateAnalyze(netParams = netParams, simConfig = simConfig)

# Play sound when done:
os.system('say "script is done"')