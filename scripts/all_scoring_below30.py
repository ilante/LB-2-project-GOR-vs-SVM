def lines_to_list(infile1): 
    ''' Reads all lines from a file and saves them to a list. '''
    content_list = []
    with open(infile1, "r") as rfile:
        content_list = rfile.readlines()
        return content_list
        
below = lines_to_list("id_below_30.hits")  # list of all ids scoring below 30% id
above = lines_to_list('id_above_30.hits')  # list of all ids scoring above and equal to 30% id

def remove_matches(lower, higher):
    '''Takes two lists as input and returns a list that contains
    all values of 'lower' values that are NOT element of 'higher'.'''
    keepers = []          # list holding all ids that have not scored >= 30% with any of the JPRED sequnces
    for i in lower:       
        if i not in higher: 
            keepers.append(i)  # keeps only ids that are not reported in the list "above"
    return keepers

keep = remove_matches(below, above) 

# print(len(keep))
# Have 177 unique sequnces with no match above 30% id with any other sequ in the testing (JPRED) set.

##########################################################
# Making a list of all ids (input IDs of the blastp)
##########################################################

all_ids = lines_to_list("best_of_final_cluster") # generating list of all ids that were in the blastp input
# print(len(all_ids))

def keep_mis_matches(biglist, partiallist):
    '''Stores exclusively biglist values that are not reported in partiallist.
    Returns the biglist with all partiallist matches removed. Keeps all values 
    that donot match any element of partiallist in a new list. Returns the new list.'''
    keepers = []
    for i in biglist:
        if i not in partiallist:
            keepers.append(i) 
    return keepers

all_without_above = keep_mis_matches(all_ids, above)
# len(all_without_above)

def write_list_to_file(liste, newfile):
    '''Takes as input a list and writes each element to a new file'''
    with open(newfile, 'a') as afile: 
        for i in liste:
            afile.write(i)
            
write_list_to_file(all_without_above, 'try_again')
