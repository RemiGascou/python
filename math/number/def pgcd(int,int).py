# PGCD ENTRE 2 NOMBRES
def pgcd(a,b):
        while b: a, b = b, a%b
        return a
