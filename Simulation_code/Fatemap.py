__author__ = "Mark Xiang"
__created__ = "09/01/2023"
__updated__ = "08/21/2024"

##----------- Import packages --------------##
import numpy as np
import matplotlib.pyplot as plt
##----------- Import functions --------------##
from  Print_memory_usage import print_memory_usage

##----------- Define functions --------------##
class fatemap():
    '''define fatemap death_threshold, reentry_threshold (and differentiation_threshold)'''
    def __init__(self, model = None):
        if model == 0: # Theoratical model without differentiation, leaving out differentiation_threshold.
            self.death_threshold =           [0.0500, 0.0500, 0.0500, 0.0500, 0.0500, 0.0500, 0.0500, 0.0500, 0.0500]
            self.reentry_threshold =         [0.0500, 0.1500, 0.5500, 0.8800, 0.9600, 0.9920, 0.9990, 0.9998, 1.0000]
            self.differentiation_threshold = [1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000]
        elif model == 10: # Theoratical model with differentiation, including differentiation_threshold.
            self.death_threshold =           [0.0500, 0.0500, 0.0500, 0.0500, 0.0500, 0.0500, 0.0500, 0.0500, 0.0500]
            self.reentry_threshold =         [0.0500, 0.1400, 0.5300, 0.8600, 0.9200, 0.9380, 0.9460, 0.9495, 0.9500]
            self.differentiation_threshold = [0.9500, 0.9500, 0.9500, 0.9500, 0.9500, 0.9500, 0.9500, 0.9500, 0.9500]
        # different models with differentiation
        elif model == 11: # Model with differentiation 1%
            self.death_threshold =           [0.0500 / 0.95 * 0.99] * 9
            self.reentry_threshold =         [r / 0.95 * 0.99 for r in [0.0500, 0.1400, 0.5300, 0.8600, 0.9200, 0.9380, 0.9460, 0.9495, 0.9500]]
            self.differentiation_threshold = [0.9900] * 9
        elif model == 12: # Model with differentiation 2%
            self.death_threshold =           [0.0500 / 0.95 * 0.98] * 9
            self.reentry_threshold =         [r / 0.95 * 0.98 for r in [0.0500, 0.1400, 0.5300, 0.8600, 0.9200, 0.9380, 0.9460, 0.9495, 0.9500]]
            self.differentiation_threshold = [0.9800] * 9
        elif model == 13: # Model with differentiation 3%
            self.death_threshold =           [0.0500 / 0.95 * 0.97] * 9
            self.reentry_threshold =         [r / 0.95 * 0.97 for r in [0.0500, 0.1400, 0.5300, 0.8600, 0.9200, 0.9380, 0.9460, 0.9495, 0.9500]]
            self.differentiation_threshold = [0.9700] * 9
        elif model == 14: # Model with differentiation 4%
            self.death_threshold =           [0.0500 / 0.95 * 0.96] * 9
            self.reentry_threshold =         [r / 0.95 * 0.96 for r in [0.0500, 0.1400, 0.5300, 0.8600, 0.9200, 0.9380, 0.9460, 0.9495, 0.9500]]
            self.differentiation_threshold = [0.9600] * 9
        elif model == 15: # Model with differentiation 5%
            self.death_threshold =           [0.0500 / 0.95 * 0.95] * 9
            self.reentry_threshold =         [r / 0.95 * 0.95 for r in [0.0500, 0.1400, 0.5300, 0.8600, 0.9200, 0.9380, 0.9460, 0.9495, 0.9500]]
            self.differentiation_threshold = [0.9500] * 9
        elif model == 16: # Model with differentiation 6%
            self.death_threshold =           [0.0500 / 0.95 * 0.94] * 9
            self.reentry_threshold =         [r / 0.95 * 0.94 for r in [0.0500, 0.1400, 0.5300, 0.8600, 0.9200, 0.9380, 0.9460, 0.9495, 0.9500]]
            self.differentiation_threshold = [0.9400] * 9
        elif model == 17: # Model with differentiation 7%
            self.death_threshold =           [0.0500 / 0.95 * 0.93] * 9
            self.reentry_threshold =         [r / 0.95 * 0.93 for r in [0.0500, 0.1400, 0.5300, 0.8600, 0.9200, 0.9380, 0.9460, 0.9495, 0.9500]]
            self.differentiation_threshold = [0.9300] * 9
        elif model == 18: # Model with differentiation 8%
            self.death_threshold =           [0.0500 / 0.95 * 0.92] * 9
            self.reentry_threshold =         [r / 0.95 * 0.92 for r in [0.0500, 0.1400, 0.5300, 0.8600, 0.9200, 0.9380, 0.9460, 0.9495, 0.9500]]
            self.differentiation_threshold = [0.9200] * 9
        elif model == 19: # Model with differentiation 9%
            self.death_threshold =           [0.0500 / 0.95 * 0.91] * 9
            self.reentry_threshold =         [r / 0.95 * 0.91 for r in [0.0500, 0.1400, 0.5300, 0.8600, 0.9200, 0.9380, 0.9460, 0.9495, 0.9500]]
            self.differentiation_threshold = [0.9100] * 9
        elif model == 20: # Model with differentiation 10%
            self.death_threshold =           [0.0500 / 0.95 * 0.90] * 9
            self.reentry_threshold =         [r / 0.95 * 0.90 for r in [0.0500, 0.1400, 0.5300, 0.8600, 0.9200, 0.9380, 0.9460, 0.9495, 0.9500]]
            self.differentiation_threshold = [0.9000] * 9
        elif model == 21: # Model with differentiation 12%
            self.death_threshold =           [0.0500 / 0.95 * 0.88] * 9
            self.reentry_threshold =         [r / 0.95 * 0.88 for r in [0.0500, 0.1400, 0.5300, 0.8600, 0.9200, 0.9380, 0.9460, 0.9495, 0.9500]]
            self.differentiation_threshold = [0.8800] * 9
        elif model == 22: # Model with differentiation 14%
            self.death_threshold =           [0.0500 / 0.95 * 0.86] * 9
            self.reentry_threshold =         [r / 0.95 * 0.86 for r in [0.0500, 0.1400, 0.5300, 0.8600, 0.9200, 0.9380, 0.9460, 0.9495, 0.9500]]
            self.differentiation_threshold = [0.8600] * 9
        elif model == 23: # Model with differentiation 16%
            self.death_threshold =           [0.0500 / 0.95 * 0.84] * 9
            self.reentry_threshold =         [r / 0.95 * 0.84 for r in [0.0500, 0.1400, 0.5300, 0.8600, 0.9200, 0.9380, 0.9460, 0.9495, 0.9500]]
            self.differentiation_threshold = [0.8400] * 9
        elif model == 24: # Model with differentiation 18%
            self.death_threshold =           [0.0500 / 0.95 * 0.82] * 9
            self.reentry_threshold =         [r / 0.95 * 0.82 for r in [0.0500, 0.1400, 0.5300, 0.8600, 0.9200, 0.9380, 0.9460, 0.9495, 0.9500]]
            self.differentiation_threshold = [0.8200] * 9
        elif model == 25: # Model with differentiation 20%
            self.death_threshold =           [0.0500 / 0.95 * 0.80] * 9
            self.reentry_threshold =         [r / 0.95 * 0.80 for r in [0.0500, 0.1400, 0.5300, 0.8600, 0.9200, 0.9380, 0.9460, 0.9495, 0.9500]]
            self.differentiation_threshold = [0.8000] * 9
        # different models with death
        elif model == 26: # Model with death 1%
            self.death_threshold =           [0.0100] * 9
            self.reentry_threshold =         [1 - ((1 - r) / 0.95 * 0.99) for r in [0.0500, 0.1400, 0.5300, 0.8600, 0.9200, 0.9380, 0.9460, 0.9495, 0.9500]]
            self.differentiation_threshold = [1 - ((1 - 0.9500) / 0.95 * 0.99)] * 9
        elif model == 27: # Model with death 3%
            self.death_threshold =           [0.0300] * 9
            self.reentry_threshold =         [1 - ((1 - r) / 0.95 * 0.97) for r in [0.0500, 0.1400, 0.5300, 0.8600, 0.9200, 0.9380, 0.9460, 0.9495, 0.9500]]
            self.differentiation_threshold = [1 - ((1 - 0.9500) / 0.95 * 0.97)] * 9
        elif model == 28: # Model with death 5%
            self.death_threshold =           [0.0500] * 9
            self.reentry_threshold =         [1 - ((1 - r) / 0.95 * 0.95) for r in [0.0500, 0.1400, 0.5300, 0.8600, 0.9200, 0.9380, 0.9460, 0.9495, 0.9500]]
            self.differentiation_threshold = [1 - ((1 - 0.9500) / 0.95 * 0.95)] * 9
        elif model == 29: # Model with death 8%
            self.death_threshold =           [0.0800] * 9
            self.reentry_threshold =         [1 -((1 - r) / 0.95 * 0.92) for r in [0.0500, 0.1400, 0.5300, 0.8600, 0.9200, 0.9380, 0.9460, 0.9495, 0.9500]]
            self.differentiation_threshold = [1 - ((1 - 0.9500) / 0.95 * 0.92)] * 9
        elif model == 30: # Model with death 20%
            self.death_threshold =           [0.2000] * 9
            self.reentry_threshold =         [1 - ((1 - r) / 0.95 * 0.80) for r in [0.0500, 0.1400, 0.5300, 0.8600, 0.9200, 0.9380, 0.9460, 0.9495, 0.9500]]
            self.differentiation_threshold = [1 - ((1 - 0.9500) / 0.95 * 0.80)] * 9
        # different models with experimental data
        elif model == 31: # HVN054_136h_FW (Fixed, WT)
            self.death_threshold =           [0.1033, 0.0959, 0.1320, 0.1840, 0.2459, 0.3193, 0.3971, 0.4657, 0.6588]
            self.reentry_threshold =         [0.1546, 0.2052, 0.3687, 0.5304, 0.6247, 0.6782, 0.7139, 0.7578, 0.9613]
            self.differentiation_threshold = [0.9674, 0.9443, 0.9615, 0.9762, 0.9758, 0.9680, 0.9566, 0.9505, 0.9613]
        elif model == 32: # HVN054_136h_FN (Fixed, nfkb1-KO)
            self.death_threshold =           [0.2550, 0.2907, 0.3001, 0.3351, 0.3978, 0.4589, 0.5140, 0.5190, 0.5947]
            self.reentry_threshold =         [0.2883, 0.3689, 0.4260, 0.5335, 0.6458, 0.7154, 0.7577, 0.8086, 0.9952]
            self.differentiation_threshold = [0.9861, 0.9703, 0.9775, 0.9886, 0.9954, 0.9961, 0.9974, 0.9955, 0.9952]
        elif model == 33: # HVN054_136h_FA (Fixed, IkBa-mut/mut)
            self.death_threshold =           [0.0314, 0.0983, 0.3081, 0.5526, 0.6557, 0.6323, 0.5783, 0.5392, 0.7172]
            self.reentry_threshold =         [0.0644, 0.1715, 0.3899, 0.6178, 0.7329, 0.7546, 0.7416, 0.7137, 0.8889]
            self.differentiation_threshold = [0.9902, 0.9854, 0.9756, 0.9583, 0.9363, 0.9034, 0.8747, 0.8576, 0.8889]
        else:
            raise ValueError('orz: model must be given')

##----------- Simulation --------------##
if __name__ == "__main__":
    print_memory_usage("Fatemap.py is running.")