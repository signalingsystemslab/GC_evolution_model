__author__ = "Mark Xiang"
__created__ = "09/01/2023"
__updated__ = "08/14/2024"

##----------- Import functions --------------##
from Fatemap import fatemap
from Print_memory_usage import print_memory_usage

##----------- Define functions --------------##
def fateDecision(recycle, death, reenter, plasma, model):
    #print_memory_usage('Fate Decision started ...')
    divider = []
    for bcell in recycle:
        generation = bcell.generation
        fitnessScore = bcell.fitnessScore
        death_threshold, reentry_threshold, differentiation_threshold = fateThreshold(generation, model)
        if 0 <= fitnessScore < death_threshold:
            death.append(bcell)
        elif death_threshold <= fitnessScore <= reentry_threshold:
            reenter.append(bcell)
        elif reentry_threshold < fitnessScore <= differentiation_threshold:
            divider.append(bcell)
        elif differentiation_threshold < fitnessScore <= 1:
            plasma.append(bcell)
        else:
            raise ValueError('orz: fateScore must be within [0, 1]')
    #print_memory_usage('Fate Decision finished.')
    return(death, reenter, divider, plasma)

def fateThreshold(generation, model):
    fate = fatemap(model = model)
    return(fate.death_threshold[generation], fate.reentry_threshold[generation], fate.differentiation_threshold[generation])

##----------- Simulation --------------##
if __name__ == "__main__":
    print_memory_usage("FateDecision.py is running.")