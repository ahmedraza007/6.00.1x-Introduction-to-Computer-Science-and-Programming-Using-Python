import string


def string_todict(lc, shift):
    d = dict()
    for i in range(len(lc)):
        try:
            d[lc[i]] = lc[i+shift]
        except IndexError:
            if (i + shift) >= 25:
                j = (i + shift) - 25
                d[lc[i]] = lc[j - 1]
            continue
    return d


def mergedicts(d, f):
    return dict(d.items() + f.items())


def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.
  
    shift: 0 <= int < 26
    returns: dict
    """
    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    d = string_todict(lc, shift)
    f = string_todict(uc, shift)
    q = mergedicts(d,f)
    return q
        
    
# r = buildCoder(9)
# print len(r)
# print r



# lc = string.ascii_lowercase
# d = string_todict(lc, 3)
# uc = string.ascii_uppercase
# f = string_todict(uc, 3)
# print len(d)
# print d
# print len(f)
# print f
# q = mergedicts(d, f)
# print q
# print len(q)
