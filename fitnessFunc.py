## Calculate the fitness of a solution (based on .json file)

from statistics import median, mean
import json
import pandas as pd

with open('data/25mN-CD.json', 'rb') as mechData: mechData = json.load(mechData)

fitnessData = mechData['simData']

def fitnessFunc(simData, **kwargs):
    PRO1 = []
    PRO2 = []
    PRO3 = []
    PRO4 = []
    for i in range(399, 409): # spikes of projection neurons for network 01 (50 mN)
        spkt01_ = len([spkt for spkt, spkid in zip(simData['spkt'], simData['spkid']) if spkid == i])
        PRO1.append(spkt01_)
    for i in range(808, 818): # spikes of projection neurons for network 02 (100 mN)
        spkt23_ = len([spkt for spkt, spkid in zip(simData['spkt'], simData['spkid']) if spkid == i])
        PRO2.append(spkt23_)
    for i in range(1217, 1227): # spikes of projection neurons for network 03 (200 mN)    
        spkt45_ = len([spkt for spkt, spkid in zip(simData['spkt'], simData['spkid']) if spkid == i])
        PRO3.append(spkt45_)
    for i in range(1626, 1636): # spikes of projection neurons for network 03 (10 mN)    
        spkt67_ = len([spkt for spkt, spkid in zip(simData['spkt'], simData['spkid']) if spkid == i])
        PRO4.append(spkt67_)

    if PRO1 == []:PRO1.append(0)
    if PRO2 == []:PRO2.append(0)
    if PRO3 == []:PRO3.append(0)
    if PRO4 == []:PRO4.append(0)

    # Firing Rate (total # of spikes / 5 seconds):
    numSec = 5 # sim length (s)
    PRO1s = [x/numSec for x in PRO1] 
    PRO2s = [x/numSec for x in PRO2] 
    PRO3s = [x/numSec for x in PRO3] 
    PRO4s = [x/numSec for x in PRO4] 
    # Median Firing Rate:
    med_PRO1 = median(PRO1s)
    med_PRO2 = median(PRO2s)
    med_PRO3 = median(PRO3s)
    med_PRO4 = median(PRO4s)
    # Mean Firing Rate:
    mean_PRO1 = mean(PRO1s)
    mean_PRO2 = mean(PRO2s)
    mean_PRO3 = mean(PRO3s)
    mean_PRO4 = mean(PRO4s)

    if med_PRO1 == 0 or med_PRO2 == 0 or med_PRO3 == 0:
        fitness = 10000
    else:
        fitness = abs((1.63 - med_PRO1)/1.63) + abs((5.46 - med_PRO2)/5.46) + abs((9.70 - med_PRO3)/9.70) + abs(0 - med_PRO4)

    return PRO1s, PRO2s, PRO3s, PRO4s, fitness

# Fitness of 
fitness = fitnessFunc(fitnessData)

# Print results:
# print('fitness =',fitness[4])
print('Median =',fitness[0])
# print('Mean =',fitness[5])
# print('Median (100mN) =',fitness[1])
# print('Median (200mN) =',fitness[2])
# print('Median (10mN) =',fitness[3])












