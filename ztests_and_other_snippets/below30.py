# #!/usr/bin/env python3
# import sys

# def idfile_to_list = 

def file_to_list(id_infile1):
    id_list = []
    with open(id_infile1) as rfile:
        for line in rfile:
            clean = rfile.readline().rstrip()
            id_list.append(clean)
    return id_list
    
ids = file_to_list('ids')
prcnt = file_to_list('percentage')
print(ids, prcnt)

# def keep_below30(idlist, numlist):
#     keepID = []
#     keepNum = []
#     for i in range(len(numlist)):
#         num = float(numlist[i])
#         print(type(num))
#         if num <= 30:
#             keepID.append(idlist[i])
#             keepNum.append(float(numlist[i]))
#     print(keepID, keepNum)
            
# keep_below30(ids, prcnt)            


# if __name__ == '__main__':
#     infile = sys.argv[1]
#     outfile = sys.argv[2]
    
#     # CALL FUNCITOJN

