def split_list(liste):
    ''' Splits a evennumbered list into two lists. id_list contains all odd items while seq_list contains all even items. Returns the two lists.'''
    id_list = liste[::2]
    seq_list = liste[1::2]
    return id_list, seq_list

# teste = ['a', 'b', 'c', 'd', 'e', 'f'] #Works
ids, seq = split_list(myfastalist)
