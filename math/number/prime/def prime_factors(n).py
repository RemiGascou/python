from time import *

def prime_factors(n):
    factors = []
    for k in range(2,n+2):
        while n % k == 0:
            factors.append(k)
            n = n//k
    return factors

n = int(input("Prime factors of : "))

tic = clock()

print("Prime factors of number",n,"are :",prime_factors(n))

tac = clock()

print("Time elapsed :",int((tac-tic)*10000)/10000," seconds.")