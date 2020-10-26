#!/anaconda3/bin/python
import sys
import os
import pandas as pd
import numpy as np
import argparse 

'''For the first try: Make function: Takes fasta and dssp sequence as parameters as input.'''
# d1g2ya_.dssp
# d1g2ya_.fasta from training files.

# win_size = 3 # has to be an odd number pass through argparse later
# num_rows = win_size*4 #adapts to desired window size

def make_zero_array():
    '''
    Takes window size and the name of the array as arguments.
    Makes an array that has as many lines as the win_size and 
    the number of columns is defined by the number of naturally 
    occurring aa in eukaryotes. Returns the array.
    '''
    array = np.zeros((1,20)) #, dtype= 'float64' is allready default - not necessary to specify!!!
    return array
    
R_H = make_zero_array()           # generating arrays holding the counts of residue in conformation X --> R_X
R_E = make_zero_array()
R_C = make_zero_array()
R_count = make_zero_array()       # generating array holding the total residue count
SS_count = make_zero_array()      # generating array holding the total secondary structure count

def make_frequency_df(zeroarray):
    '''
    Makes dataframe from zero array to better vizualize whats going on.
    That enables us to index columns by residue name.
    '''
    header_col = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
    row_names = ['R_0'] #['#R,H', '#R,E', '#R,C', '#R'] # want to implement using -1 0 1 according to window....
#     freq_array = make_zero_array(win_size)
    freq_df = pd.DataFrame(data = zeroarray,  columns=header_col, index=row_names)
    return freq_df

''' generating dataframes holding the counts of residue in conformation X --> R_X'''
df_R_H = make_frequency_df(R_H)           
df_R_E = make_frequency_df(R_E)
df_R_C = make_frequency_df(R_C)
df_R_count=make_frequency_df(R_count)
# df_SS_count = make_frequency_df(SS_count)     

''' generating smaller datafram holding the total counts conformations'''
ss_array = np.zeros((1,3)) # making array holding total n of R in H, E or C
df_all_SS = pd.DataFrame(data=ss_array, columns=['H', 'E', 'C'], index= ['#S'])
# print("HEC df")
# print(df_all_SS)

def read_clean_lines(infile1):
    ''' Reads all lines from a file. Returns string of second line. The '\n' is stripped.'''
    with open(infile1, 'r') as rfile:
        newline_list = rfile.readlines()
        cleanstring = newline_list[1].rstrip()
        return cleanstring

def train_gor(aafile, ssfile, RH, RE, RC, total_R, total_SS):
    '''
    Takes fasta and ss from dssp file and dataframes comprising the gor model (RH, RE, RC, total_R and total_SS).
    Increments corresponding positions according to R and H in each field. Returns the trained GOR model.
    '''
    aa_string = read_clean_lines(aafile)
    print(aa_string)
    ss_string = read_clean_lines(ssfile)
    print(ss_string)

    l = len(aa_string)

    for i in range(l):
        ss = ss_string[i]                   # name of structure at index i
        aa = aa_string[i]                   # name of residue at index i
        total_R[aa]+=1                      # Incrementing each df
        
        if ss == 'H':
            RH[aa]+=1
            total_SS[ss]+=1
        elif ss == 'E':
            RE[aa]+=1
            total_SS[ss]+=1
        else:                               # so if ss == '-' or ss == 'C' or even if i got some X:
            RC[aa]+=1
            total_SS['C']+=1                # If not H or E --> its assigned to 'C' compatible with training and blind files.
    return RH, RE, RC, total_R, total_SS

# aa_path = '/Users/ila/01-Unibo/02_Lab2/files_lab2_project/all_data/trainingset/fasta/d1g2ya_.fasta'
# ss_path = '/Users/ila/01-Unibo/02_Lab2/files_lab2_project/all_data/trainingset/dssp/d1g2ya_.dssp'

parser = argparse.ArgumentParser(description='Train GOR model')
parser.add_argument('-f', '--fasta', type=str, metavar='', required=True, help='Path to directory containing all fasta files needed for training.')
parser.add_argument('-s', '--secondarystructure', type=str, metavar='', required=True, help='Path to directory containing all secondary structures in fasta-like format needed for training.')
args = parser.parse_args()

if __name__ == '__main__':
    fastafiles = os.listdir(args.fasta) # Creating list of all fasta files in folder
    ss_files = os.listdir(args.secondarystructure) # Creating list of all ss structure files
    # listdir: returns arbitrary order --> need to sort lists before continuing --> MUST .sort()
    fastafiles.sort()
    ss_files.sort()
    # print(type(args.fasta))
    # print(args.secondarystructure)
    
    '''
    2 lists --> to loop on. Need to call function to loop on both aa and ss list.
    For now print all models. >> to file in cmd line for now.
    '''
    for i in range(len(fastafiles)):
        train_gor(args.fasta+'/'+fastafiles[i], args.secondarystructure+'/'+ss_files[i], df_R_H, df_R_E, df_R_C, df_R_count, df_all_SS)

    print("R_H")
    print(df_R_H)
    print("R_E")
    print(df_R_E)
    print("R_C")
    print(df_R_C)
    print("total Residue count")
    print(df_R_count)
    print('Conformation counts')
    print(df_all_SS)
