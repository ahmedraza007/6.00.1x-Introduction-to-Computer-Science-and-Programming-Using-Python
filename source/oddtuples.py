def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    g = ()
    for i in range(len(aTup)):
        if i%2 != 0:
            print i
            continue
        else:
            
            g = g + (aTup[i],)
            print "g " , g
    return g


print oddTuples((4, 15, 4, 5, 2, 15, 7, 20))