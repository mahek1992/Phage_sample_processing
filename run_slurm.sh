#!/usr/bin/env bash

#SBATCH --job-name="8_il10_2"
#SBATCH --nodelist=ws4
#SBATCH --partition=high
#SBATCH --cpus-per-task=8
#SBATCH --mem=10G
#SBATCH --time=14-00:00:00
#SBATCH --output=slurm_small-test-32cpu_%A_%a_%j.log

echo
dt1=$(date '+%Y/%m/%d %H:%M:%S')
echo -e "---- $dt1 ---- " | tee -a times.log

python consensus_calling_nonumi.py

echo; dt1=$(date '+%Y/%m/%d %H:%M:%S')
echo -e "---- $dt1 ---- " | tee -a times.log
