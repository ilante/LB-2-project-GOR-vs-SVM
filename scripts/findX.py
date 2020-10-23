

def lines_list(infile1):                                              # call list of file names and for dsspfile
    ''' Reads all lines from a file and saves them to a list. '''
    with open(infile1) as ofile:
        flist = ofile.readlines() # returns list containing each line of the file
        return flist
    
def findX(filename):
    with open(filename+".fasta") as myfasta:
        id = myfasta.readline()
        sequ = myfasta.readline()
        if 'A' in sequ == True:
            print(filename, sequ)

id_chain = lines_list('/Users/ila/01-Unibo/02_Lab2/project_blindset/blindset_all_PDBs/150_blind_PDBs/BLINDset_id_and_chain')              

for el in id_chain:            # each el is like "6LTZ:A"
    field_list = el.split(':') # list  BOTH contains ID [0] and chain [1]
    fname_id =  field_list[0].lower()                   #
#     fname = "pdb"+field_list[0].lower()+".ent.dssp"     #fname to be used in the function calls
    chain = field_list[1].rstrip()                             # chain name to be used in each function call
    findX(fname_id)        

