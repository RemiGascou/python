#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
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

def isPrime(n):
    if n <= 1 :
        return False
    else :
        for k in range(2,int(n**(0.5)+1)):
            if n % k == 0:
                return False
        return True

import sys
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage : python3 "+sys.argv[0]+" outfile MAXI")
    else :
        outfile = sys.argv[1]
        maxi = int(sys.argv[2])
        open(outfile, "w").close() # Create the file
        for k in range(3, maxi, 2):
            if (k+1) % (maxi//10) == 0 : print("[LOG] Currently at "+str(round((k+1)/(maxi//10), 2))+"%  ")
            if isPrime(n):
                f = open(outfile, "a")
                f.write(str(n)+"\n")
                f.close()
