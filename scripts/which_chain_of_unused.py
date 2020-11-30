def lines_list(infile1):                                              # call for list of file names AND for dsspfile
    ''' Reads all lines from a file and saves them to a list. '''
    nonewline = []
    with open(infile1) as ofile:
        raw_list = ofile.readlines() # returns list containing each line of the file
        for el in raw_list:
            nonewline.append(el.rstrip())
    return nonewline
    
all_160 = lines_list("/Users/ila/01-Unibo/02_Lab2/files_lab2_project/all_data/blindset/blindset_all_PDBs/150_blind_PDBs/all_160_ids_and_chains_blindset")    
wanted_no_chain = lines_list("/Users/ila/01-Unibo/02_Lab2/files_lab2_project/all_data/blindset/blindset_all_PDBs/150_blind_PDBs/unused_10/ids_of_unused_10")

def lower_clean_list(list1):
    ''' 
    Takes id list. Returns list of ids from even valued pos
    and chain list for odd valued positions.
    '''
    names_lower = []
    chains_upper = []
    list_of_splits = []
    for i in list1:
        sp_li = i.split(':')
        names_lower.append(sp_li[0].lower())
        chains_upper.append(sp_li[1]) #.rstrip()
    return names_lower, chains_upper

def dict_from_2_lists(list1, list2):
    '''
    Takes 2 lists as input and returns a dictionary where items 
    from list1 are keys and items from list2 are the values.
    '''
    keys = list1
    values = list2
    dictionary = dict(zip(list1, list2))
    return dictionary

def find_position(dict1, list_no_chains):
    for el in list_no_chains:
        print(el+':'+dict1[el])

# Calling functions
my_dictionary = dict_from_2_lists(a,b)
find_position(my_dictionary,wanted_no_chain)
    