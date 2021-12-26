# Simulation of the SDH Network Model
## 1. Install all necessary packages:
```
pip install netpyne
pip install neuron
pip install mpi4py
```
## 2. Clone ```SDH-network``` repo

## 3. Run the network model (one stimulus intensity/simulation):
### Step 1: Compile the mod files
```
> cd ~/SDH-network
> nrnivmodl
```
### Step 2A: Initialize and simulate the network (without MPI)
```
> ipython
>> run init_mechanical.py  
```
Files used are ```cfg_mechanical.py``` (configuration parameters), ```netParams_mechanical.py``` (network parameters), ```cells.py``` (cell types and attributes), ```genrn.py``` (generic neuron template), ```spkt_gen.py```, plus .JSON files for primary afferent spike trains and .mod files for spinal neurons.

### Step 2B: Initialize and simulate the network (with MPI)
```
> ipython
>> mpiexec -np X nrniv -python -mpi init_mechanical.py  
```
Where ```X``` is the number of nodes you want to use.
