def lines_to_list(filename):
    ''' Reads all lines from a file and saves them to a list. '''
    content_list = []
    with open(filename, "r") as rfile:
        content_list = rfile.readlines()
        return content_list

# mylist = lines_to_list("nospace.fasta")  #works
