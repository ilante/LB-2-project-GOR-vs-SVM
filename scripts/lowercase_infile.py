#!/anaconda3/bin/python
import sys
import os

# script to check if there are any lowercase letters corresponding to SS bridges (Cysteins).
def find_lowerletters(infile1):
    ''' 
    Reads lines from a file  EXCLUDING line 1. Saves string to a variable.
    Checks each character. If character is lower case it is replaced by a C. As all dssp files designate
    SS-bridges with lower case pairs.
    '''
    with open(infile1) as ofile:
        lines = ofile.readlines()
        header = lines[0]
        sequence = lines[1] # list of each line of the file excluding line 0  
        upper_seq = ''
    # check_string = lines_list(infile1)[0] # l[0] to check_string
    for char in sequence:
        if char.isupper():
            upper_seq += char
        if char.islower():      # if any of the letters is lower case
            upper_seq += 'C'    # all lower are converted to cysteins
            print(infile1)      # to see how which files I got in my set
    return header, upper_seq

def write_upper(infile1):
    '''
    Calls find_lowerletters and writes what it returns 
    the same file truncating it.
    '''
    header, upper_seq = find_lowerletters(infile1)
    with open(infile1, 'w') as wfile:
        wfile.write(header+upper_seq)          #need to make new files or over write
        wfile.truncate()
    return 

def ids_list(infile2):                                              # call list of file names and for dsspfile
    ''' Reads all lines from a file and saves them to a list. '''
    cleanlines_list = []
    with open(infile2) as ofile:
        flist = ofile.readlines()# list of each line of the file excluding line 0 
        for line in flist:
            nonewline = line.rstrip()
            cleanlines_list.append(nonewline)
        return cleanlines_list

if __name__ == '__main__':
    ids_path = sys.argv[1]
    ids = ids_list(ids_path)        # "./list_of_blindset_ids_only"
    blind_set_path = sys.argv[2]
    for ID in ids:
        write_upper(os.path.join(blind_set_path, ID+".fasta"))
