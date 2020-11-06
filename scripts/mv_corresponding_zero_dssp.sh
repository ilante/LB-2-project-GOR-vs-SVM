#!/bin/bash

# Making new dir to store zero profiles
mkdir /Users/ila/01-Unibo/02_Lab2/files_lab2_project/all_data/blindset/blind_zero_profiles/

# Moving 'zero_profiles' to new folder
cat /Users/ila/01-Unibo/02_Lab2/files_lab2_project/all_data/blindset/seqprofile_blind/zero_profile_list | while read i;
    do 
        mv "$i" /Users/ila/01-Unibo/02_Lab2/files_lab2_project/all_data/blindset/blind_zero_profiles/ 
    done
