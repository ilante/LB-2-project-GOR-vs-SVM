#!/usr/bin/env python3
import sys
import os.path

def pssm_list(infile):                                              # call list of file names and for dsspfile
    ''' Reads relevant lines from a pssm file and saves them to a list.
    Returns values of the 2 matrices (no header).'''
    with open(infile) as ofile:
        flist = ofile.readlines()[3:-6] # list of each line of the file excluding first 3 & last 6 lines
        return flist

def lines_to_list(infile1):
        ''' Reads all lines from a file and saves them to a list containing the '\n' char. '''
        all_lines_list = []
        with open(infile1, 'r') as rfile:
            all_lines_list = rfile.readlines()
        return all_lines_list  # need to rstrip in a loop for using filenames.
        
def relevant_lines(infile2):
    '''Takes list (extracted from a .pssm file) and extracts the Sequence Profile Portion only.
    Returns a list of list where each element is one line of the sequence profile matrix. '''
    pssm_profile_list = pssm_list(infile2)     # contains all lines from the pssm file.           
    profile_final_list = []                # for holding relevant fileds of the line
    for line in pssm_profile_list:
            pssm_profile_list = line.split()[22:42]   # profile ranges from pos 22-42 
            profile_final_list.append(pssm_profile_list) # appending to final list of lists
    return profile_final_list # list of lists
    
# # devide all values by 100   
def write_normalized_profile(profile_final_list, ofile):
    '''Takes profile list of lists and outfile name as input. Writes each number that is in 
    one of the sublists and devides it by 100. The number is converted to a string and added
    a tab and written to a file. After each sublist a newline character is written to the file.'''
    with open(ofile, "a") as wfile:
        for sublist in profile_final_list:
#             print(sublist)
            for el in sublist:
                num =int(el)/100
                numstring=str(num)
                wfile.write(numstring+'\t')  # adding tab after each number
            wfile.write("\n")                # adding newline at the end of each sublist.

if __name__ == '__main__':
    infile1 = sys.argv[1] # the idlist to loop on
    #Call the function by looping through an id list+'.pssm' extension
    # name the outfile the same --> id list+'.profile'
    idlist = lines_to_list(infile1)  # containing the id of the file but NOT the extension ".pssm" 
    for ids in idlist:
        infile = '/home/um19/project/psiblast_output_all_fasta/'+ ids.rstrip()+'.psiblast.pssm'    # removing newlinecharacter, adding necessary extension
        if os.path.isfile(infile) == True:       # does this file exist?
            ofile = ids.rstrip()+'.profile'    # outifile for each id with correct extension
            profile_list = relevant_lines(infile)
            write_normalized_profile(profile_list, ofile)
        else:
            print("Error file: "+infile+" not found.")
