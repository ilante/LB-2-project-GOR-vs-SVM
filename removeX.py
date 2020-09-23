#!/usr/bin/env python3
import sys

def lines_to_list(filename):
    ''' Reads all lines from a file and saves them to a list. '''
    content_list = []
    with open(filename, "r") as rfile:
        content_list = rfile.readlines()
        return content_list



def split_list(filename):
    ''' Splits a evennumbered list into two lists. id_list contains 
    all odd items while seq_list contains all even items. Returns the two lists.'''
    myfastalist = lines_to_list(filename)  #works
    id_list = myfastalist[::2]
    seq_list = myfastalist[1::2]
    return id_list, seq_list

# teste = ['a', 'b', 'c', 'd', 'e', 'f'] #Works
# ids, seq = split_list()
# print(len(ids))
# print(len(seq)) #works

def remove_X(filename):
    '''Removes items containing X in the sequence list but also the ID in the ID list. 
    Returns an ID list and an'''
    id1, seq2 = split_list(filename)
    noXid = []
    noXseq = []
    for i in range(len(id1)):
        flag = "X" in seq2[i]
        if flag == False:
            noXid.append(id1[i])
            noXseq.append(seq2[i])
    return noXid, noXseq

# i , s = remove_X()  # works
# print(len(i))
# print(len(s))   

def no_X_id_and_seq(filename):
    ''' Joins the lists to a big list containing both id and sequences. Returns one big list'''
    id_list, seq_list = remove_X(filename)
    biglist = []
    for i in range(len(id_list)):
        biglist.append(id_list[i])
        biglist.append(seq_list[i])
    return biglist

# a = no_X_id_and_seq()
# print(len(a))

def list_to_fasta(infile, outfile):
    '''Calls no_X_id_and_seq() and uses this list.
     Writes all elements i to 
    a file. Returns the file.'''
    liste = no_X_id_and_seq(infile)
    with open(outfile, 'w') as F:
        for i in liste:
            F.write(str(i))
    F.close  

if __name__ == '__main__':
    infile = sys.argv[1]
    outfile = sys.argv[2]
    list_to_fasta(infile, outfile)

