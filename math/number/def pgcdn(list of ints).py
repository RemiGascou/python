# PGCD ENTRE PLUS QUE 2 NOMBRES
def pgcdn(*n):
    """Calcul du 'Plus Grand Commun Diviseur' de n (>=2) valeurs entières (Euclide)"""
    def _pgcd(a,b):
        while b: a, b = b, a%b
        return a
    p = _pgcd(n[0], n[1])
    for x in n[2:]:
        p = _pgcd(p, x)
    return p
