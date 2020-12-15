import sys, os
import numpy as np

#Create a list of lists from tab separated txt file.
#@input: a tab separated txt file containing a profile with no amminoacid line.
#@output: a list of lists.
def create_list (profile_file):
    pro_matrix=[]
    for line in profile_file:
        line= line.rstrip().split("\t")
        pro_matrix.append(line)    
    return(pro_matrix)

#Compute the input file of LIBSVM 
#@input Profile matrix, window size and dssp file
#@output file in the format for SVM analysis
def create_vector (pro_matrix, wsize, dssp):
    #for each element of dssp file
    for i in range(len(dssp)):
        #assing the secondary structure to a variable
        sec_str= dssp[i]
        #environment initialisation
        vector=[]
        line=""
        hw= int((wsize-1)/2)
        #create a range from central position (i) minus half window size to the central position plus half window size.
        for z in range(i-hw,i+(hw+1)):
            #check for position not corresponding to profile lines and skip them.
            if z<0 or z>(len(pro_matrix)-1): continue
            #if we are in a correct line of the window.
            else:
                #add the line in the list vector
                vector.extend(pro_matrix[z])
        #transform the vector in a numpy array
        vector= np.array(vector, dtype=float)
        #for each element of the vector
        for el in range(len(vector)):
            #if we are in the starting position
            if el==0:
                #and the secondary structure is alpha elic
                if sec_str=="H":
                    #assign the corresponding label
                    line+= "1 "
                #and the secondary structure is beta sheet
                elif sec_str=="E":
                    #assign the corresponding label
                    line+= "2 "
                #and the secondary structure is coil
                elif sec_str=="-" or sec_str=="C":
                    #assign the corresponding label
                    line+= "3 "
                #check if the element is different from zero
                if vector[el]!=0.0:
                    #add the position and the value to the string
                    line+= str(el+1) + ":" + str(vector[el]) + " "
            #if we are not in positon zero
            else:
                #check if the element is different from zero
                if vector[el]!=0.0:
                    #add the position and the value to the string (starts from 0 which it SHOULDNT) but since we have trained the models already - it is too late.
                    line+= str(el) + ":" + str(vector[el]) + " "
        #add the line in the file
        f.write(line + "\n")
        #reset line and vector
        line=""
        vector=[]                
#part of the code to take input from terminal
#Command line: python3 SVMinput.py --input ID list --extension .txt --path path to the input directory --windowsize 17 --output svmvectors.dat
if __name__ == '__main__':
    #check for number of inputs
    if len(sys.argv)==11:
        #file containing protein IDs
        Pids= sys.argv[2]
        #extension of profile files
        ext= sys.argv[4]
        #path to the directory of the inpur files
        path= sys.argv[6]
        #window size
        window= int(sys.argv[8])
        #file output name
        file_output= sys.argv[10]
        #check for odd window
        if window//2==0:
            #print error
            print("Window must be odd")
            exit()
    #if the input is not correct.
    else:
        #print example
        print("Example of proper input: python3 SVMinput.py --input fileslist.txt --extension .txt --path profile-data --windowsize 17 --output svmvectors.dat")

#initialise error file
# error=open("./standard_error" + Pids, "a")
with open("./standard_error", "a") as error:
#open file output in append mode
    # f=open(file_output, "a")
    with open(file_output, "a") as f:
        #open IDs file in read mode
        # o_Pids= open(Pids,"r") 
        with open(Pids, 'r') as o_Pids:
            #for each ID in the file
            for line in o_Pids:
                #avoid the new line character
                line = line.rstrip()
                #check the existance of dssp file
                print('***', path + "/" + line + ".dssp")
                if os.path.isfile(path + "/" + line + ".dssp"):
                    #open dssp file
                    dssp_file = open(path + "/" + line + ".dssp","r")
                    #check for line different from header
                    for el in dssp_file:
                        if el[0]!=">":
                            #save the string into a variable without new line
                            dssp= el.rstrip()
                    #open the profile of the ID
                    raw_pro= open(path + "/" + line + ext, "r")
                    print(path + "/" + line + ext)
                    #compute the matrix
                    matrix_p=create_list(raw_pro)
                    #add the profile in vectorial form
                    create_vector(matrix_p, window, dssp)
                #if dssp file does not exist
                else:
                    #write error in the erroti file
                    error.write("No profile for this ID: " + line + "\n")