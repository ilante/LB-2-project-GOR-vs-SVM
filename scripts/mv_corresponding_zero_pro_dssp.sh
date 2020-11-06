#!/bin/bash

# Making new dir to store fasta like dssp files corresponding to missing profiles
mkdir /Users/ila/01-Unibo/02_Lab2/files_lab2_project/all_data/trainingset/trainingset_removed_zero_pro_dssps/

# Moving dssp files corresponding to 'zero_profiles' to new folder
# Run in sending directory!!!
cat /Users/ila/01-Unibo/02_Lab2/files_lab2_project/all_data/trainingset/missing_ids_pssm_files_traininset_ids_ONLY | while read i;
    do 
        mv "$i" /Users/ila/01-Unibo/02_Lab2/files_lab2_project/all_data/trainingset/trainingset_removed_zero_pro_dssps/
    done
