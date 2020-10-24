#!/bin/bash
# Running the DSSP on the extracted PDB files
for i in *.ent
do
	mkdssp -i "$i" -o "./dsspout/$i.dssp"
done
