def wsd(n):
    sum = 0
    k = 0
    n = abs(n)
    while n >= 10**k:
        k = k + 1
    for p in range(k-1,-1,-1):
        digit = int(n/10**p)
        weight = (k-p)
        n = n - digit * 10**p
        sum = sum + digit*weight
    return sum

# HIGHLY PACKED VERSION :

def wsd2(n):
    sum,k,n = 0,0,abs(n)
    while n >= 10**k:
        k = k + 1
    for p in range(k-1,-1,-1):
        sum = sum + int(n/10**p)*(k-p)
        n = n - int(n/10**p)* 10**p
    return sum

print(wsd2(1492))
print(wsd2(1776))
print(wsd2(1))