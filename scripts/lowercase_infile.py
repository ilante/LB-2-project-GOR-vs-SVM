# script to check if there are any lowercase letters corresponding to SS bridges (Cysteins).
def lines_list(infile1):                                              # call list of file names and for dsspfile
    ''' Reads lines from a file  EXCLUDING line 1 and saves them to a list. '''
    cleanlines_list = []
    with open(infile1) as ofile:
        flist = ofile.readlines()[1:] # list of each line of the file excluding line 0 
        for line in flist:
            nonewline = line.rstrip()
            cleanlines_list.append(nonewline)
        return cleanlines_list

def find_lowerletters(infile1):
    check_string = lines_list(infile1)[0] # l[0] to check_string
    if check_string.islower():     # if any of the letters is lower case
        print(infile1)
# #     else: 
# #         continue
#     print("all caps")
# print(lines_list("./blind_fasta/4ywn.fasta")[0]) # works
# find_lowerletters("./blind_fasta/4ywn.fasta")

def ids_list(infile2):                                              # call list of file names and for dsspfile
    ''' Reads all lines from a file and saves them to a list. '''
    cleanlines_list = []
    with open(infile2) as ofile:
        flist = ofile.readlines()# list of each line of the file excluding line 0 
        for line in flist:
            nonewline = line.rstrip()
            cleanlines_list.append(nonewline)
        return cleanlines_list
    

ids = ids_list("./list_of_blindset_ids_only")

for ID in ids:
    find_lowerletters('./blind_fasta/'+ID+".fasta")
    