def isPrime(n):
    if n<= 1 :
        return False
    else :
        for k in range(2,int(n**(0.5)+1)):
            if n % k == 0:
                return False
        return True