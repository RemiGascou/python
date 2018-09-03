##__init__.py generator :

import os, sys

def tab(varname:str, data:list):
    if len(data) != 0:
        out = varname + """ = ["""
        data.sort()
        for e in data[:-1]:
            if type(e) == str:  out += "\n\t\"" + str(e) + '\",'
            if type(e) == int:  out += "\n\t"   + str(e) + ','   
        if type(e) == str:      out += "\n\t\"" + str(data[-1]) + '\"'
        if type(e) == int:      out += "\n\t"   + str(data[-1])
        out += "\n]"
    else :
        out = varname + """ = []"""
    return out

def import_all(working_dir:str):
    return [file[:-3] for file in os.listdir(working_dir) if file.endswith(".py") and not file.startswith("__")]

working_dir = r"D:\Projets GIT\Quetzal\QuetzalProject"


var_all_import = tab("__all__", import_all(working_dir))
print(var_all_import)

