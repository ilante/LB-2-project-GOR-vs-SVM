def lines_list(infile1):                                              # call list of file names and for dsspfile
    ''' Reads all lines from a file and saves them to a list. '''
    with open(infile1) as ofile:
        flist = ofile.readlines() # returns list containing each line of the file
        return flist

def relevant_lines(infile1, desired_chain):
    '''Takes list (extracted from a DSSP file) and the name of the desired_chain as input.
    Returns 2 strings: ss_string holds the secondary structure mapping and aa_string holds 
    the amino acid information. Missing residues (when no atomic information of the PDB is 
    present) are assigned the letter "C" (coil) in the ss_string and "X" in the aa_string.'''
    dssp_list = lines_list(infile1)     # contains all lines from the dssp file.
    relevant = False # boolean variable            
#     desired_chain = "A"                            # change to load from "id_and_chain_blindset2"
    ss_string = ''
    aa_string = ''
    for line in dssp_list:
        if '#' in line: # find last line before relevant output
            relevant =True   # flips rel to true - so the folowing lines are saved
            continue
        if relevant:
            if line[11] == desired_chain:
                ss_string += line[16]
                if line[13] == "!":
                    aa_string += "X"
                else:
                    if line[13].islower() == True:          # residues forming C-C bridges are indicated with lower case letters
                        aa_string += 'C'                    # residues forming C-C bridges are indicated with lower case letters
                    else:
                        aa_string += line[13]
    return ss_string, aa_string

def raw_to_threclasses(rawstring):
        structure_dict = {"H":"H", "G":"H", "I":"H", "B":"E", "E":"E", "T":"C", "S":"C", " ":"C"} 
        threeclasses = ''
        for letter in rawstring:
                threeclasses += structure_dict[letter]
        return threeclasses    
    
def generate_dssp_fasta(filename_id, chain): 
    '''Writes SS to dsspfile and AA to fastafile'''
    # reads dssp file and returns ss_string and aa_string.
    ss_string, aa_string = relevant_lines("/Users/ila/01-Unibo/02_Lab2/project_blindset/deletechainmess/testruns/pdb"+filename_id+".ent.dssp", chain)     
    with open(filename_id+".dssp", 'w') as dsspfile:
        ss = raw_to_threclasses(ss_string)
        dsspfile.write(">"+filename_id+"_"+chain+"\n")
        dsspfile.write(ss+"\n")
        
    with open(filename_id+".fasta", 'w') as fastafile:    
        fastafile.write(">"+filename_id+"_"+chain+"\n")
        fastafile.write(aa_string+"\n")
        if aa_string == "":
                print('empty',filename_id, chain, end="")
        
# creating list holding all pdb ids and chain descriptions        
id_chain = lines_list('/Users/ila/01-Unibo/02_Lab2/project_blindset/myBLINDset_id_and_chain')  

for el in id_chain:            # each el is like "6LTZ:A"
    field_list = el.split(':') # list  BOTH contains ID [0] and chain [1]
    fname_id =  field_list[0].lower()                   #
#     fname = "pdb"+field_list[0].lower()+".ent.dssp"     #fname to be used in the function calls
    chain = field_list[1].rstrip()                             # chain name to be used in each function call
    generate_dssp_fasta(fname_id, chain)
