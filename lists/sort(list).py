#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : 
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*

def sort_ins(list_in):
    buffer,sorted = [],[list_in[0]]
    for element in list_in[1:]:
        for s in sorted:
            if s < element:
                buffer.append(s)
            else:
                buffer.append(element)
                buffer.append(s)
        sorted = buffer
    return sorted

print(sort_ins([1,5,7,3,1,2,2,6,4,8,9,13,11]))
