def genPrimes():
    prime = []
    x = 1
    while True:
        x += 1
        for p in prime:
            if x % p == 0:
                break
        else:
            prime.append(x)
            yield x
            
gen = genPrimes()
print gen.next()
print gen.next()
print gen.next()
print gen.next()