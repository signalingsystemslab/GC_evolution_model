__author__ = "Mark Xiang"
__created__ = "09/01/2023"
__updated__ = "08/14/2024"

##----------- Import packages --------------##
import numpy as np
from scipy.stats import norm, lognorm
import matplotlib.pyplot as plt
##----------- Import functions --------------##
from  Print_memory_usage import print_memory_usage

##----------- Define functions --------------##
class Bcells(object):
    '''B-cells that in their cell fate decision and selection process'''
    cellID = 0
    
    def __init__(self, affinity = None, parent = None, founder = None, cyclefounder = None, generation = None, GCR = None, mutation_depth = None, productive_mutation_depth = None, non_productive_mutation_depth = None, ifitnessScore = None, fitnessScore = None):
        self.cellID = Bcells.cellID
        Bcells.cellID += 1
        self.affinity = affinity
        self.parent = parent
        self.founder = founder
        self.cyclefounder = cyclefounder
        self.generation = generation
        self.GCR = GCR
        self.mutation_depth = mutation_depth
        self.ifitnessScore = ifitnessScore
        self.fitnessScore = fitnessScore

def resetBcells():
    Bcells.cellID = 0

def initializeBcells(size = 50, type = "normal", loc = 11.5, scale = 0.33, shape = None):
    print_memory_usage('initialization started ...')
    resetBcells()
    affinity = norm.rvs(loc=loc, scale=scale, size=size) # Basal condition: affinity = norm.rvs(loc = 11.5, scale = 0.33, size = nb)
    affinity = list(affinity)
    affinity.sort(reverse = True)
    affinity = np.array(affinity)
    parent = np.zeros(size, dtype = "int")-1
    founder = np.arange(0, size, 1, dtype="int")
    cyclefounder = np.arange(0, size, 1, dtype="int")
    GCR = np.zeros(size, dtype = "int")-1
    mutation_depth = np.zeros(size, dtype = "int")
    bcells = [Bcells(affinity = affinity[i], parent = parent[i], founder = founder[i], cyclefounder = cyclefounder[i], GCR = GCR[i], mutation_depth = mutation_depth[i]) for i in range(size)]    
    print_memory_usage('initialization finished.')
    return(bcells)

def GCsize(t): # Size of the germinal center in µm^2 and density measurement adapted from Figure 2C, 2F. Wittenbrink et. al. JI. 2011. PMID: 22102720.
    GCsize = [4167, 5410, 8088, 10767, 13445, 15100, 16754, 18409, 20063, 20300, 20536, 20772, 21008, 21087, 21165, 21244, 21323, 20116, 18908, 17700, 16492, 15967, 15442, 14917, 14391, 13971, 13550, 13130, 12710, 12518, 12325, 12133, 11940, 11748, 11555]
    if t > 34:
        size = 11555 - (14391-11555)/(34-24)*(t-34)
    else:
        size = GCsize[t]
    n = int(size/1000*12)
    return(n)

##----------- Simulation --------------##
if __name__ == "__main__":
    print_memory_usage("Initialization.py is running.")
    plt.rcParams['axes.labelsize'] = 24
    plt.rcParams['axes.titlesize'] = 32
    plt.rc('xtick', labelsize=24)
    plt.rc('ytick', labelsize=24)

    import seaborn as sns
    import pandas as pd
    #Plot the size of the germinal center
    # Generate data
    t_list = []
    n_list = []

    for t in range(40):
        t_list.append(t)
        n_list.append(GCsize(t))

    # Create a dataframe
    data = pd.DataFrame({'Time': t_list, 'GCsize': n_list})

    for labeled in [True, False]:
        # Plot using seaborn
        plt.figure(figsize=(20, 20), dpi=500)
        ax = sns.lineplot(x='Time', y='GCsize', data=data, marker='o', linewidth=5, color='black', markersize = 12)
        ax.set_xlim(-0.05, 40.05)
        ax.set_xticks([0, 20, 40])
        ax.set_ylim(-0.1, 300.1)
        ax.set_yticks([0, 150, 300])
        if not labeled:
            ax.set_xticklabels(['', '', ''])
            ax.set_yticklabels(['', '', ''])
        # Save the plot
        plt.savefig(f'GCSize_labeled{labeled}.png', dpi=500, bbox_inches='tight')
        plt.close()
    