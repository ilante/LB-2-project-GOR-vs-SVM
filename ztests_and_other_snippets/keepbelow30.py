def lowsimilarity(id_list, percent_list):
    lowsimilairty_ids = []
    lowsimilarity_percentage = []
    for i in range(len(percent_list)):
        if float(lowsimilarity_percentage[i]) < 30:
            lowsimilairty_ids += id_list
            lowsimilarity_percentage += float(lowsimilarity_percentage[i])
    return lowsimilairty_ids, lowsimilarity_percentage

    
lowsimilarity(ids, identity_percent)
ids=[5EV3:A,5EV2:A,5EV4:A,5FMP:AB,5EYO:AC,5ITH:A,5IWM:BD,5IWI:BD,]
identity_percent=[30.159,30.159,30.159,30.108,54.717,33.333,46.341,46.341,]
ids=[5EV3:A,5EV2:A,5EV4:A,5FMP:AB,5EYO:AC,5ITH:A,5IWM:BD,5IWI:BD,]
ids=[  ,  ,  ,  ,  ,  ,  ,  ,]
