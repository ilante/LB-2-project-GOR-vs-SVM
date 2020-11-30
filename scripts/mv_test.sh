#!/bin/bash
# Moving the training files to corresponding folder
mkdir test/
for i in {0..4}
do
    f="SVM_TrainSet${i}_TestSet${i}.txt"
	mv "$f" /Users/ila/01-Unibo/02_Lab2/files_lab2_project/all_data/inputs/SVM_inputs/test/
done
