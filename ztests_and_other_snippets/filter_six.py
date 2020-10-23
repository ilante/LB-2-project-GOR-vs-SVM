def filter_short(infile, outfile):
    del_seq_index = []
    lines_list = []
    with open(infile) as rfile:
        lines_list = rfile.readlines()
        for i in range(1, len(lines_list),2):
            if len(lines_list[i]) < 7:
                del_seq_index.append(i-1) # appending header index
                del_seq_index.append(i)   # appending sequence index
    with open(outfile, 'w') as wfile:
        for i in range(len(lines_list)):
            if i in del_seq_index:
                continue
            wfile.write(lines_list[i])    
        
filter_short("no_X.fasta", 'longsequences.fasta')                   