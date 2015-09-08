from math import log
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    a = 0
    #f = True
    while (True):
        if (b**a) == x:
            break
        elif (b**a) >= x:
            a = a - 1
            break
        a = a + 1 
    return a

print myLog(16,2)
print myLog(15,3)
print myLog(33,2)
print log(16,2)