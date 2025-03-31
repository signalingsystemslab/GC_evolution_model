__author__ = "Mark Xiang"
__created__ = "09/01/2023"
__updated__ = "03/01/2024"

##----------- Import packages --------------##
import argparse
import numpy as np
##----------- Import functions --------------##
from Print_memory_usage import print_memory_usage
from Initialization import resetBcells, initializeBcells, GCsize
from Selection import selection
from Mutation import DividerSHM
from FateDecision import fateDecision

##----------- Simulation --------------##
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simulate B-cell affinity maturation')
    parser.add_argument('-m', '--model', type=int, default=10, required=False, help='whether to include PC in the model')
    parser.add_argument('-s', '--stochasticity', type=float, default=0, required=False, help='value for stochasticity')
    parser.add_argument('-hr', '--heritability', type=float, default=0, required=False, help='value for epigenetic heritability')
    parser.add_argument('-pm', '--mutation_rate', type=float, default=0.5, required=False, help='mutation rate for SHM')
    parser.add_argument('-mc', '--monte_carlo_repeat', type=int, required=True, help='monte carlo repeat ID')
    parser.add_argument('-o', '--out_dir', required=True, help='output directory')
    args = parser.parse_args()
    model = args.model
    s = args.stochasticity
    if s == 1:
        s -= 0.0000001
    h = args.heritability
    if h == 1:
        h -= 0.0000001
    mc = args.monte_carlo_repeat
    pm = args.mutation_rate
    out_dir = args.out_dir

    print_memory_usage(f'Model {model}, S = {s}, h = {h}, repeat {mc} is running ...')
    # Monte Carlo simulation w/ a comlete cycle for GCR
    nb = 50
    nc = 42
    resetBcells()
    reentry = []
    select = []
    failselect = []
    plasma = []
    death = []
    division = []
    lethal = []
    average_division = []
    reenter = initializeBcells(size = nb)
    for t in range(nc): #Affinity Selection Cycling
        selectionSize = GCsize(t)
        #print_memory_usage(f'GC size in cycle {t} is {selectionSize}')
        recycle, reentry, select, failselect = selection(reenter, reentry, select, failselect, s, h, selectionSize)
        select_cellcounts = len(recycle)
        
        reenter = []
        i = 0 #Inertial Cycling
        while len(recycle):
            death, reenter, divider, plasma = fateDecision(recycle, death, reenter, plasma, model)
            i += 1
            if not len(divider): # Termination of inertial cycling
                break
            recycle, division, lethal = DividerSHM(divider, recycle, division, lethal, s, h, pm)
        
        #print_memory_usage(f'In cycle {t}, reentry size is {len(reentry)} with cellID {[bcell.cellID for bcell in reentry]}')
        avg_div = round(np.log2(len(reenter)/select_cellcounts), 2)
        average_division.append(avg_div)
        #print_memory_usage(f'In cycle {t}, the average number of divisions is depicted by {len(reenter)} = {select_cellcounts} * 2 ^ {avg_div}')

        if not len(reenter): # Termination of affinity selection cycling
            print_memory_usage(f"No b-cells will reenter for selection and GCR failed at cycle {t}.")
            break
    aveDiv = round(np.mean(average_division), 2)
    with open(out_dir + f'/sim_model{model:02d}_s{s:.3f}_h{h:.3f}_pm{pm:.2f}_mc{mc:03d}_aveDiv{aveDiv:.2f}.txt', mode = 'x') as f: # Open a file for writing
        f.write('type\tcellID\taffnty\tmDpth\tparent\tfounder\tcfder\tgenrtn\tGCR\tifScore\tfScore\n') # Write the header line
        for bcell in select: # Loop through the bcells and write their attribute values to the file
            f.write(f'select\t{bcell.cellID}\t{bcell.affinity:.4f}\t{bcell.mutation_depth}\t{bcell.parent}\t{bcell.founder}\t{bcell.cyclefounder}\t{bcell.generation}\t{bcell.GCR}\t{bcell.ifitnessScore:.4f}\t{bcell.fitnessScore:.4f}\n')
        for bcell in failselect:
            f.write(f'fail\t{bcell.cellID}\t{bcell.affinity:.4f}\t{bcell.mutation_depth}\t{bcell.parent}\t{bcell.founder}\t{bcell.cyclefounder}\t{bcell.generation}\t{bcell.GCR}\t{bcell.ifitnessScore:.4f}\t{bcell.fitnessScore:.4f}\n')
        for bcell in division:
            f.write(f'divide\t{bcell.cellID}\t{bcell.affinity:.4f}\t{bcell.mutation_depth}\t{bcell.parent}\t{bcell.founder}\t{bcell.cyclefounder}\t{bcell.generation}\t{bcell.GCR}\t{bcell.ifitnessScore:.4f}\t{bcell.fitnessScore:.4f}\n')
        for bcell in lethal:
            f.write(f'lethal\t{bcell.cellID}\t{bcell.affinity:.4f}\t{bcell.mutation_depth}\t{bcell.parent}\t{bcell.founder}\t{bcell.cyclefounder}\t{bcell.generation}\t{bcell.GCR}\t{bcell.ifitnessScore:.4f}\t{bcell.fitnessScore:.4f}\n')
        for bcell in death:
            f.write(f'death\t{bcell.cellID}\t{bcell.affinity:.4f}\t{bcell.mutation_depth}\t{bcell.parent}\t{bcell.founder}\t{bcell.cyclefounder}\t{bcell.generation}\t{bcell.GCR}\t{bcell.ifitnessScore:.4f}\t{bcell.fitnessScore:.4f}\n')
        if model >= 10:
            for bcell in plasma:
                f.write(f'plasma\t{bcell.cellID}\t{bcell.affinity:.4f}\t{bcell.mutation_depth}\t{bcell.parent}\t{bcell.founder}\t{bcell.cyclefounder}\t{bcell.generation}\t{bcell.GCR}\t{bcell.ifitnessScore:.4f}\t{bcell.fitnessScore:.4f}\n')
        for bcell in reentry:
            f.write(f'reentry\t{bcell.cellID}\t{bcell.affinity:.4f}\t{bcell.mutation_depth}\t{bcell.parent}\t{bcell.founder}\t{bcell.cyclefounder}\t{bcell.generation}\t{bcell.GCR}\t{bcell.ifitnessScore:.4f}\t{bcell.fitnessScore:.4f}\n')
