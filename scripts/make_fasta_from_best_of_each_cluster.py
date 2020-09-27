#!/usr/bin/env python3
import sys

def lines_to_list(infile1): 
    ''' Reads all lines from a file and saves them to a list. '''
    content_list = []
    with open(infile1, "r") as rfile:
        content_list = rfile.readlines()
        return content_list

def split_list(infile1):
    ''' Splits a evennumbered list into two lists. id_list contains 
    all odd items while seq_list contains all even items. Returns the two lists.'''
    myfastalist = lines_to_list(infile1)  #works
    id_list = myfastalist[::2]
    seq_list = myfastalist[1::2]
    return id_list, seq_list

def dict_from_lists(infile1):
    '''Takes feeds two lists into a dictionary. 
    Returns the dicitonary'''
    id_list, seq_list = split_list(infile1)
    keys = id_list
    values = seq_list
    full_dict = dict(zip(keys, values))
    return full_dict

def keep_whats_in_dict(infile1, infile2, outfile):
    '''Loops through a list and a dictionary. Appending the values
    of the list (PDB ids which are also the keys of the dictionary) and the
    values of the dictionary to the outfile.'''
    idlist = lines_to_list(infile2) # reading ids from file into list
    aa_dict = dict_from_lists(infile1)
    with open(outfile, 'a') as afile:
        for i in idlist:
            afile.write(i) #appending ID in even lines
            afile.write(aa_dict[i]) # appending value (sequ) in odd lines

if __name__ == '__main__':
    infile1 = sys.argv[1]
    infile2 = sys.argv[2]
    outfile = sys.argv[3]
    keep_whats_in_dict(infile1, infile2, outfile)
