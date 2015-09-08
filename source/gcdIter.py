def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if (a < b):
        g = a
    else:
        g = b
    while (g != 0):
        if ((a % g == 0) and (b % g == 0)):
            return g
        else:
            g = g - 1
            continue
        
print gcdIter(2,12)
print gcdIter(17,12)
print gcdIter(6,12)
print gcdIter(9,12)
print gcdIter(8,45)