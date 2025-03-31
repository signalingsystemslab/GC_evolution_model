__author__ = "Mark Xiang"
__created__ = "09/01/2023"
__updated__ = "08/14/2024"

##----------- Import packages --------------##
import numpy as np
import random
import matplotlib.pyplot as plt
##----------- Import functions --------------##
from Selection import updateFitnessScore
from Initialization import Bcells
from  Print_memory_usage import print_memory_usage

##----------- Define functions --------------##
def DividerSHM(divider, recycle, division, lethal, s, h, mrate):
    #print_memory_usage('Mutation started ...')
    recycle = []
    for bcell in divider:
        affinity = bcell.affinity
        parent = bcell.cellID
        founder  = bcell.founder
        cyclefounder = bcell.cyclefounder
        generation = bcell.generation + 1
        mutation_depth = bcell.mutation_depth
        GCR = bcell.GCR
        ifitnessScore = bcell.ifitnessScore
        fitnessScore = bcell.fitnessScore
        affinity_variance = 0.08 #measured from average affinity variance # affinity_variance = bcell.initial_affinity_variance
        sigma = max(np.sqrt(affinity_variance/float((1-s*(1-h))**2) - affinity_variance), 0.0000001)
        fitnessScore1 = round(updateFitnessScore(fitnessScore, sigma), 6)
        fitnessScore2 = round(updateFitnessScore(fitnessScore, sigma), 6)
        bcell1 = Bcells(affinity = affinity, parent = parent, founder = founder, cyclefounder = cyclefounder, generation = generation, GCR = GCR, mutation_depth = mutation_depth, ifitnessScore = ifitnessScore, fitnessScore = fitnessScore1)
        bcell2 = Bcells(affinity = affinity, parent = parent, founder = founder, cyclefounder = cyclefounder, generation = generation, GCR = GCR, mutation_depth = mutation_depth, ifitnessScore = ifitnessScore, fitnessScore = fitnessScore2)
        
        recycle, lethal = SHM(bcell1, bcell2, recycle, lethal, mrate) # Perform SHM
        division.append(bcell)
    #print_memory_usage('Mutation finished.')
    return(recycle, division, lethal)

def SHM(bcell1, bcell2, recycle, lethal, pm):
    m1 = np.random.random()
    if m1 < pm:
        recycle.append(bcell1)
    else:
        prob = np.random.random() # Probability adapted from Shannon and Mehr. J Immunol Baltim Md 1950. 1999. PMID: 10201914.
        if prob < 0.28125:
            lethal.append(bcell1)
        elif prob > 1 - 0.1875:
            pdfdE, pdfPdE = affinityImprovementData()
            dE = random.choices(pdfdE, pdfPdE)[0] + np.random.random()*0.8-0.4
            bcell1.affinity = round(max(1, bcell1.affinity - dE), 6)
            bcell1.mutation_depth = bcell1.mutation_depth + 1
            recycle.append(bcell1)
        else:
            bcell1.mutation_depth = bcell1.mutation_depth + 1
            recycle.append(bcell1)
    m2 = np.random.random()
    if m2 < pm:
        recycle.append(bcell2)
    else:
        prob = np.random.random()
        if prob < 0.28125:
            lethal.append(bcell2)
        elif prob > 1 - 0.1875:
            pdfdE, pdfPdE = affinityImprovementData()
            dE = random.choices(pdfdE, pdfPdE)[0] + np.random.random()*0.8-0.4
            bcell2.affinity = round(max(1, bcell2.affinity - dE), 6)
            bcell2.mutation_depth = bcell2.mutation_depth + 1
            recycle.append(bcell2)
        else:
            bcell2.mutation_depth = bcell2.mutation_depth + 1
            recycle.append(bcell2)
    return(recycle, lethal)

# #For a more advanced SHM model, use the following code:
# def SHM(bcell1, bcell2, recycle, lethal, pm):
#     mutations = np.random.binomial(5, pm)
#     if mutations == 0:
#         recycle.append(bcell1)
#         recycle.append(bcell2)
#         return(recycle, lethal)
#     elif mutations == 1:
#         recycle.append(bcell1)
#         prob = np.random.random()
#         if prob < 0.28125:
#             lethal.append(bcell2)
#         elif prob > 1 - 0.1875:
#             pdfdE, pdfPdE = affinityImprovementData()
#             dE = random.choices(pdfdE, pdfPdE)[0] + np.random.random()*0.8-0.4
#             bcell2.affinity = max(2.6, bcell2.affinity - dE)
#             bcell2.mutation_depth = bcell2.mutation_depth + 1
#             recycle.append(bcell2)
#         else:
#             bcell2.mutation_depth = bcell2.mutation_depth + 1
#             recycle.append(bcell2)
#         return(recycle, lethal)
#     else:
#         cell1_mutation = sum(np.random.choice([0, 1], size=mutations, p=[0.5, 0.5]))
#         cell2_mutation = mutations - cell1_mutation
#         while cell1_mutation > 0:
#             prob = np.random.random()
#             if prob < 0.28125:
#                 lethal.append(bcell1)
#                 break
#             elif prob > 1 - 0.1875:
#                 pdfdE, pdfPdE = affinityImprovementData()
#                 dE = random.choices(pdfdE, pdfPdE)[0] + np.random.random()*0.8-0.4
#                 bcell1.affinity = max(2.6, bcell1.affinity - dE)
#                 bcell1.mutation_depth = bcell1.mutation_depth + 1
#             else:
#                 bcell1.mutation_depth = bcell1.mutation_depth + 1
#                 pass
#             cell1_mutation -= 1
#         if cell1_mutation == 0:
#             recycle.append(bcell1)
#         while cell2_mutation > 0:
#             prob = np.random.random()
#             if prob < 0.28125:
#                 lethal.append(bcell2)
#                 break
#             elif prob > 1 - 0.1875:
#                 pdfdE, pdfPdE = affinityImprovementData()
#                 dE = random.choices(pdfdE, pdfPdE)[0] + np.random.random()*0.8-0.4
#                 bcell2.affinity = max(2.6, bcell2.affinity - dE)
#                 bcell2.mutation_depth = bcell2.mutation_depth + 1
#             else:
#                 bcell2.mutation_depth = bcell2.mutation_depth + 1
#                 pass
#             cell2_mutation -= 1
#         if cell2_mutation == 0:
#             recycle.append(bcell2)
#         return(recycle, lethal)

def affinityImprovementData(): # Adapted from Figure 1. Zhang and Shakhnovich. PloS Comp. Biol. 2010. PMID: 20532164. PMCID: PMC2880589.
    pdfdE = [-1.62, -0.81, 0, 0.81, 1.62, 2.42, 3.23, 4.04, 4.85, 5.65, 6.46, 7.27, 8.08, 8.89, 9.69, 10.05]
    pdfPdE = [0.014, 0.034, 0.186, 0.160, 0.136, 0.096, 0.093, 0.055, 0.048, 0.036, 0.0324, 0.047, 0.0228, 0.0228, 0.012, 0.005]
    return(pdfdE, pdfPdE)

##----------- Simulation --------------##
if __name__ == "__main__":
    print_memory_usage("Mutation.py is running.")
    plt.rcParams['axes.labelsize'] = 24
    plt.rcParams['axes.titlesize'] = 32
    plt.rc('xtick', labelsize=24)
    plt.rc('ytick', labelsize=24)

    #Plot the fate map
    fig = plt.figure(figsize=(12,12), dpi = 500)
    ax = fig.add_subplot(1, 1, 1)
    plt.plot(affinityImprovementData()[0], affinityImprovementData()[1], 'o-', color = 'black', markersize = 10)
    plt.savefig('Affinity_Change.png')
