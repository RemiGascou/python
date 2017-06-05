def crible(stop):
    # Crible D'Eratosthène - Version du 19/05/2017
    facteurs_premiers, buffer_modulo, liste_nombres = [],[],[]
    for indice in range(0,stop):
        for nombre in range(100*indice+1,100*indice + 100):
            liste_nombres.append(nombre)
        for i in liste_nombres:
            for j in range(2,i):
                modulo = i % j
                buffer_modulo.append(modulo)
            if not (0 in buffer_modulo):
                facteurs_premiers.append(i)
            buffer_modulo = []
    facteurs_premiers.remove(1)
    return facteurs_premiers
