#!/bin/bash
# __author__ = "Mark Xiang"
# __created__ = "09/01/2023"
# __updated__ = "03/01/2025"

# setup directories
simID=Fig23_simulation_data
mkdir -p ./$simID

# Set invariants - do not change
scriptdir=./Simulation_code
scriptname=_Simulation.py
LOG_FILE=./_logfile_Fig23_simulation.log

# setup variables
model=10 # simulation model: 0-> no PCs; 10+ -> PCs
#s=0.00 # stochasticity
#hr=0.00 # epigenetic heritability
pm=0.5 # mutation rate

# Create a command list file
command_list=$(mktemp)

# Generate commands
for mc in {1..100}
do
    for s in 0.00 0.01 0.02 0.03 0.05 0.08 0.10 0.12 0.14 0.15 0.16 0.17 0.18 0.19 0.20 0.21 0.22 0.23 0.25 0.28 0.30 0.35 0.40 0.50 1.00
    do
        for hr in 0.00 0.50 0.70 0.75 0.80 0.85 0.88 0.90 0.92 0.94 0.95 0.96 0.97 0.98 0.99 1.00
        do
            echo "python $scriptdir/$scriptname -m $model -s $s -hr $hr -nb $nb -nc $nc -pm $pm -st $st -dist $disttype -loc $loc -scale $scale -shape $shape -mc $mc -o $simID >> $LOG_FILE 2>&1" >> $command_list
        done
    done
done

# Run commands in parallel
parallel -j 60 < $command_list

# Clean up
rm $command_list
echo "simulation finished" >> $LOG_FILE 2>&1