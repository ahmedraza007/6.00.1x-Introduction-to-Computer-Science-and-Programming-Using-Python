def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False


L = [1,2,3,4]
L1 = [1,2,3]
L2 = range(20)
L3 = [1,2,3,4,5]

e = 3
e1 = 2
e2 = 7
e3 = 4

print "search",search(L, e)
print "new search", newsearch(L, e)

print "\nsearch1",search(L1, e1)
print "new search1", newsearch(L1, e1)

print "\nsearch2",search(L2, e2)
print "new search2", newsearch(L2, e2)

print "\nsearch3",search(L3, e3)
print "new search3", newsearch(L3, e3)

