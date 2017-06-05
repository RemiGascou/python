def ppcmn(*n):
    """Calcul du 'Plus Petit Commun Multiple' de n (>=2) valeurs entières (Euclide)"""
    def _pgcd(a,b):
        while b: a, b = b, a%b
        return a
    p = abs(n[0]*n[1])//_pgcd(n[0], n[1])
    for x in n[2:]:
        p = abs(p*x)//_pgcd(p, x)
    return p

print(ppcmn(1,2,5,10,20,25,50))
