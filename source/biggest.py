def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    l = aDict.keys()
    z = []
    for i in l:
        a = len(aDict[i])
        z.append(a)
        s = z.index(max(z))
    return l[s]

print biggest({'C': [9, 19, 8, 12], 'D': [7], 'F': [], 'K': [], 'J': [], 'p': [13, 20, 5], 'R': [18]})
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print biggest(animals)
