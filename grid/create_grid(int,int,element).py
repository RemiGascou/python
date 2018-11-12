# -*- coding: utf-8 -*-

def create_grid(height,width,element):
    liste = []
    liste_row = []
    for a in range(1,height+1):
        for b in range(1,width+1):
            liste.append(element)
        liste_row.append(liste)
        liste = []
    return liste_row
