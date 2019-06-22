#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : 
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*

## Range from a to b float step.

def rangefs(a,b,f=1.0):
    out = []
    if a != b :
        element = a
        while element <= b :
            out.append(element)
            element = element + f
    return out

print(rangefs(1,3,0.5))
print(rangefs(2,1))
print(list(range(2,1)))

print(rangefs(1,1))
print(list(range(1,1)))
