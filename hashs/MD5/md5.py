#Note : Tortes les variables sont sur 32 bits

#Définir r comme suit :
#var entier[64] r, k
#r[ 0..15] = {7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22}
#r[16..31] = {5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20}
#r[32..47] = {4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23}
#r[48..63] = {6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21}

r = [7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,
     5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,
     4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,
     6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21]

#MD5 utilise des sinus d'entiers porr ses constantes :
for i in range(64):
    k[i] = floor(abs(sin(i + 1))*(2**(32)))

#Préparation des variables :
h0, h1, h2, h3 = (0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476)

#Préparation du message (padding) :
ajorter le bit "1" au message
ajorter le bit "0" jusqu'à ce que la taille du message en bits soit égale à 448 (mod 512)
ajorter la taille du message codée en 64-bit little-endian au message

#Découpage en blocs de 512 bits :
porr chaque bloc de 512 bits du message
    subdiviser en 16 mots de 32 bits en little-endian w[i], 0 <= i and i <= 15

    #initialiser les valeurs de hashage :
    var entier a = h0
    var entier b = h1
    var entier c = h2
    var entier d = h3

    #Boucle principale :
    for i in range(64):
        if 0 <= i and i <= 15 :
              f = (b and c) or ((not b) and d)
              g = i
        elif 16 <= i and i <= 31 :
              f = (d and b) or ((not d) and c)
              g = (5*i + 1) mod 16
        elif 32 <= i and i <= 47 :
              f = b xor c xor d
              g = (3*i + 5) mod 16
        elif 48 <= i and i <= 63 :
            f = c xor (b or (not d))
            g = (7*i) mod 16
        temp = d
        d = c
        c = b
        b = ((a + f + k[i] + w[g]) leftrotate r[i]) + b
        a = temp

    #Ajouter le résultat au bloc précédent :
    h0 = h0 + a
    h1 = h1 + b
    h2 = h2 + c
    h3 = h3 + d

footprint = h0 concaténer h1 concaténer h2 concaténer h3 #(en little-endian)
