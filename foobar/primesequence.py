#!/usr/bin/python
def answer(n):
    import math
    # With a concatenated list of prime numbers
    # return element n through n+5
    num = 5
    primes = [2, 3]
    #Generate list of primes, would be better to have this in
    #A file somewhere to avoid recalculating each time
    while True:
        for prime in primes:
            if num % prime == 0:
                break
        else:
            for x in xrange(2, int(math.ceil(math.sqrt(num))) + 1):
                if num % x == 0:
                    break #Exit iteration after first factor found
            else:
                primes.append(num)
        num += 1
        primeCat = "".join(str(y) for y in primes)
        if len(primeCat) >= 10005:
            break
    return primeCat[n:n+5]

print(answer(3))
