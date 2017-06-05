def nCr(n,r):
    def fact(n):
        facto = 1
        for k in range(1,n+1):
            facto = facto * k
        return facto
    return (fact(n)/(fact(r)*fact(n-r)))