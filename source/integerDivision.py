def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count


print integerDivision(5,3)
print integerDivision(10,8)
print integerDivision(11,5)
print integerDivision(-10,2)