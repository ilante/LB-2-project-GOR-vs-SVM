#!/anaconda3/bin/python
import numpy as np
import sys
from numpy import savetxt
import pandas as pd

def makeSVMfile(ids_file,ws,outfolder):
	with open(ids_file,"r")as ids:
		ids_file=ids.readlines()
		for id in ids_file:
			filename=id.rstrip()
			seqid=id.rstrip()
			with open("/Users/ila/01-Unibo/02_Lab2/files_lab2_project/all_data/blindset/seqprofile_blind/"+seqid+".profile","r")as seqprof,open("/Users/ila/01-Unibo/02_Lab2/files_lab2_project/all_data/blindset/blind_dssp/"+seqid+".dssp","r")as ss:
				proflines=seqprof.readlines()
				sslines=ss.readlines()[1]
				sslines=sslines.rstrip()
				SVMlines=[]
				array_index=np.zeros((ws,20))
				ind=1
				for i in range(ws):
					for j in range(20):
					#Creates a numpy array containing the indexes of the residue.
						array_index[i,j]=int(ind)
						ind+=1
				array_index=array_index.astype(int)
				#print(array_index)

				for linenum in range(0,len(proflines)):
					linelist=[]
					if sslines[linenum]=="H":
						linelist.append(1)
					elif sslines[linenum]=="E":
						linelist.append(2)
					else:
						linelist.append(3)
					lineindex=-1
					for i in range(((ws-1)//2),-((ws-1)//2)-1,-1):
						lineindex+=1	
						if (linenum-i)>=0 and (linenum-i)<len(proflines):
							profline=proflines[linenum-i].rstrip().split()
							for j in range(0,len(profline)):
								if profline[j]!='0.0':
									linelist.append(str(array_index[lineindex,j])+":"+str(profline[j]))
					SVMlines.append(linelist)
				SVM_df=pd.DataFrame(SVMlines,dtype=object)
				SVM_df.to_csv(outfolder+"/"+seqid+".txt",index=False, header=False,sep=' ')
				#savetxt(outfolder+"/"+seqid+".csv",SVM)
		
		return(str(len(ids_file))+" files have been saved in "+str(outfolder)+"!")

if __name__=="__main__":
	ids_file=sys.argv[1]
	ws=int(sys.argv[2])
	outfolder=sys.argv[3]
	print(makeSVMfile(ids_file,ws,outfolder))		
