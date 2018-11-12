# -*- coding: utf-8 -*-

def csv_import(path:str,log:bool = False) -> list:
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
    if log == True:
        print("File ",path,"...")
        f = open(path,'r')
        print("|   Reading file...")
        lines  = f.readlines()
        print("|   Closing file.")
        f.close()

    else :
        f = open(path,'r')
        lines  = f.readlines()
        f.close()
    print("|   Converting file...")
    data_in = [line.replace("\n","").split(";") for line in lines]
    lines = []
    for line in data_in:
        buffer = []
        for element in line:
            buffer.append(convert_csv_data(element))
        lines.append(buffer)
    print("Done !")
    return lines

csv_import("C:/Users/Admin/Desktop/TIPE/csv/bobinecentrée.csv",True)
