#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*


def gen(x, y, max_x, max_y, size=1):
    out = []
    for x_k in [x+k for k in range(-size,size+1)]:
        for y_k in [y+k for k in range(-size,size+1)]:
            if x_k >= 0 and x_k <= max_x and y_k >= 0 and y_k <= max_y:
                out.append((x_k, y_k))
    return out

x, y         = 0,0
max_x, max_y = 20, 10

r = gen(x, y, max_x, max_y)
print("Neighboors :",len(r))
print(r)
