def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    l = []
    for i in aList:
        if len(i) < 4:
            l.append(i)
        else:
            continue
    return l

aList = ["apple", "cat", "dog", "banana"]
print lessThan4(aList)