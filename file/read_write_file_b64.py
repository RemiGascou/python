#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : 
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*

import base64

img_str = """"""

def read_file_to_b64(pathtofilename=''):
    in_file = open(pathtofilename, 'rb')
    out = in_file.readlines()
    in_file.close()
    return base64.b64encode(b''.join(out))

def write_file_from_b64(b64_file:str, pathtofilename=''):
    out_file = open(pathtofilename, 'wb')
    out_file.write(base64.b64decode(b64_file))
    out_file.close()



if __name__ == '__main__':
    path = "lib/testdata/maxresdefault.jpg"
    write_file_from_b64(b64_file=read_file_to_b64(path))
