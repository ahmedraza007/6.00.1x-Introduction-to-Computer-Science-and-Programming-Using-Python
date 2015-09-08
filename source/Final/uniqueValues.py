def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    count = 0
    l = []
    l2 = []
    l3 = aDict.values()
    for key in aDict:
        count = 0
        value = aDict[key]
        for i in l3:
            if value == i:
                count += 1
            else:
                continue
        if count > 1:
            continue
        else:
            l.append(key)
        
    return sorted(l)
        
        
aDict2 = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}
aDict1 = {1: 1, 2: 1, 3: 1}
aDict = {0: 4, 9: 4, 3: 4, 5: 2, 1: 1}
print uniqueValues(aDict)