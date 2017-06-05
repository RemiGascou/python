def ppcm(a,b):
    """ppcm(a,b): calcul du 'Plus Petit Commun Multiple' entre 2 nombres entiers a et b"""
    def pgcd(a,b):
        while b: a, b = b, a%b
        return a
    if (a==0) or (b==0):
        return 0
    else:
        return (a*b)//pgcd(a,b)


print(ppcm(3,52))
