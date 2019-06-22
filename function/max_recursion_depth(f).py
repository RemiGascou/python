#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*

def max_recursion_depth(f, startingstep = 1):
    """This function return the maximum recursion depth for a given function f."""
    """/!\ Don't forget to disable verbose mode on your function as max_recursion_depth(f) is using multiples tries."""
    try :
        while startingstep > 0:
            f(startingstep)
            startingstep = startingstep + 1
    except(RuntimeError): #RuntimeError: maximum recursion depth exceeded in comparison
        print('For function : "',str(f.__name__),'" (',str(f),') :\nMaximum recursion depth reached at ', startingstep,".\nLast working recursion step : ",startingstep-1, sep="")
