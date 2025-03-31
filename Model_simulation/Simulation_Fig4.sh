#!/bin/bash
# __author__ = "Mark Xiang"
# __created__ = "09/01/2023"
# __updated__ = "03/01/2025"

# setup directories
simID=Fig4_simulation_data
mkdir -p ./$simID

# Set invariants - do not change
scriptdir=./Simulation_code
scriptname=_Simulation.py
LOG_FILE=./_logfile_Fig4_simulation.log

# setup variables
# model=10 # simulation model: 0-> no PCs; 10+ -> PCs
s=0.16 # stochasticity
hr=0.95 # epigenetic heritability
# pm=0.5 # mutation rate

# Create a command list file
command_list=$(mktemp)

#Generate commands
for mc in {1..100}
do
    for pm in 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9
    do
        for model in 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
        do
            echo "python $scriptdir/$scriptname -m $model -s $s -hr $hr -nb $nb -nc $nc -pm $pm -st $st -dist $disttype -loc $loc -scale $scale -shape $shape -mc $mc -o $simID >> $LOG_FILE 2>&1" >> $command_list
        done
    done

    pm=0.5
    for model in 26 27 28 29 30 31 32 33
    do
        echo "python $scriptdir/$scriptname -m $model -s $s -hr $hr -nb $nb -nc $nc -pm $pm -st $st -dist $disttype -loc $loc -scale $scale -shape $shape -mc $mc -o $simID >> $LOG_FILE 2>&1" >> $command_list
    done
done

# Run commands in parallel
parallel -j 60 < $command_list

# Clean up
rm $command_list
echo "simulation finished" >> $LOG_FILE 2>&1