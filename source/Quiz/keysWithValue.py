def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    l = []
    p = sorted(aDict)
    for i in p:
        if aDict[i] == target:
            l.append(i)
        else:
            continue
    return l

aDict = {'a':2, 'f':4,'b':4, 'c':4, 'd':5}
print aDict
print keysWithValue(aDict, 4)