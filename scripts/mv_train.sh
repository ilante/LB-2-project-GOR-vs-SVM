#!/bin/bash
# Moving the training files to corresponding folder
mkdir train/
for i in {0..4}
do
    f="SVM_TrainSet${i}.txt"
	mv "$f" /Users/ila/01-Unibo/02_Lab2/files_lab2_project/all_data/inputs/SVM_inputs/train/
done
