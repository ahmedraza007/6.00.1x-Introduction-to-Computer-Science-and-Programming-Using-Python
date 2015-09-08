def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    r = (N % 10)
    p = N / 10
    if p == 0:
        return N
    else:
        return sumDigits(p) + r
    
print sumDigits(1024)