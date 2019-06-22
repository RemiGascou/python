#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : 
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*

def convert_csv_data(data):
    def isFloat(s):
        try:
            float(s.replace(",","."))
            return True
        except ValueError:
            return False
    if isFloat(data):
        return float(data.replace("E","e").replace(",","."))
    if data.isalpha():
        return data
    if data.isalnum() and not data.replace("E","").isdigit():
        return data
    if data.isdigit():
        return int(data)

data_in = ["7,81E-05","15","PAPUCHE","PAPUCHE15"]
for d in data_in:
    print(convert_csv_data(d),type(convert_csv_data(d)))
