def sum_of_digits(n):
    sum,k,n = 0,0,abs(n)
    while n > 10**k:
        k = k + 1
    for p in range(k-1,-1,-1):
        digit = int(n/10**p)
        n = n - digit * 10**p
        sum = sum + digit
    return sum

print(sum_of_digits(1492))
print(sum_of_digits(1776))