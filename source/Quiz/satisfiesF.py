def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    a = L[:]
    for i in a:
        if f(i) == False:
            x = L.index(i)
            L.pop(x)
            continue
        else:
            continue
    return len(L)

def f(s):
    return 'a' in s
      
L = ['bus', 'bss', 'kaeer', 'anhi','aaa']
print satisfiesF(L)
print L