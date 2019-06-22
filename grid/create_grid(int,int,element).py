#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : 
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*

def create_grid(height,width,element):
    liste = []
    liste_row = []
    for a in range(1,height+1):
        for b in range(1,width+1):
            liste.append(element)
        liste_row.append(liste)
        liste = []
    return liste_row
