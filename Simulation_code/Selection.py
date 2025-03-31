__author__ = "Mark Xiang"
__created__ = "09/01/2023"
__updated__ = "08/14/2024"

##----------- Import packages --------------##
import numpy as np
from scipy.stats import truncnorm
from copy import copy
##----------- Import functions --------------##
from  Print_memory_usage import print_memory_usage

##----------- Define functions --------------##
def selection(reenter, reentry, select, failselect, s, h, selectionSize):
    reenter.sort(key = lambda x: x.affinity, reverse = True) # Affinity from high to low
    totalAffinity = sum([bcell.affinity for bcell in reenter[0:min(selectionSize, len(reenter))]])
    cumulatedAffinity = totalAffinity
    rank = 0
    recycle = []
    affinity = []
    while len(reenter):
        bcell = reenter.pop(0)
        if bcell.GCR != -1:
            reentry.append(copy(bcell))
        
        if rank <= selectionSize:
            bcell.GCR += 1
            bcell.generation = 0
            bcell.ifitnessScore = cumulatedAffinity/totalAffinity
            bcell, cumulatedAffinity = assignInitialFitnessScore(bcell, cumulatedAffinity, s, h)
            affinity.append(bcell.affinity)
            recycle.append(bcell)
            select.append(copy(bcell))
        else:
            failselect.append(bcell)
        rank += 1
    return(recycle, reentry, select, failselect)

def assignInitialFitnessScore(bcell, cumulatedAffinity, s, h):
    ifitnessScore = bcell.ifitnessScore
    affinity_variance = 0.08 # measured from average affinity variance # affinity_variance = np.var(affinities)
    sigma = max(np.sqrt(affinity_variance/((1-s)**2) - affinity_variance), 0.0000001) # S = 1 - r, where r is pearson correlation coefficient
    fitnessScore = updateFitnessScore(ifitnessScore, sigma)
    bcell.fitnessScore = fitnessScore
    bcell.cyclefounder = bcell.cellID
    cumulatedAffinity -= bcell.affinity
    return(bcell, cumulatedAffinity)

def updateFitnessScore(fitnessScore, sigma):
    lower, upper = 0.0, 1.0
    return(truncnorm((lower - fitnessScore) / sigma, (upper - fitnessScore) / sigma, loc=fitnessScore, scale=sigma).rvs())

##----------- Simulation --------------##
if __name__ == "__main__":
    print_memory_usage("Selection.py is running.")