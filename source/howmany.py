def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    l = aDict.keys()
    z = 0
    for i in l:
        a = len(aDict[i])
        z = z + a
    return z


print howMany({'C': [9, 19, 8, 12], 'D': [7], 'F': [], 'K': [], 'J': [], 'p': [13, 20, 5], 'R': [18]})