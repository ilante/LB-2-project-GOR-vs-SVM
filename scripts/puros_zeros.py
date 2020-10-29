#!/anaconda3/bin/python
import sys
import os
import numpy as np
import pandas as pd

def profiles_array(infile1):
    '''
    Reads profile files into df. Transforms df into array.
    Adds all numbers of array. Returns file path if sum of 
    ALL array elements == 0.
    '''
    df = pd.read_csv(infile1, sep='\t', header=None) # col 20 contains NaN only
    df2 = df.drop(df.columns[-1], axis=1)          # dropping col -1 filled with NaN
    array1 = df2.to_numpy()
    zero_sum = 0
    for i in array1:
        for j in i:
            zero_sum += j
    if zero_sum == 0:
        print(infile1)
        
if __name__ == '__main__':
    path = sys.argv[1]
    profiles = os.listdir(path) # Creating list of all profile files in folder --> listdir: returns arbitrary order
    # need to make path
    for name in profiles:
        profiles_array(os.path.join(path,name))
        