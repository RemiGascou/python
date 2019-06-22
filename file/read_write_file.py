#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*

def readfile(file, binary=False):
    if binary : b_opt="b"
    else:       b_opt=""
    f = open(file, "r"+b_opt)
    data = f.readlines()
    f.close()
    return data

def writefile(file, data, binary=False):
    if binary : b_opt="b"
    else:       b_opt=""
    f = open(file, "w"+b_opt)
    for e in data:
        f.write(e)
    f.close()
    return data


readfile("0-2001000.primes",True)
#file_read("0-2001000.primes",False)
