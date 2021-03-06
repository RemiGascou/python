#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*


def parity_bit(sbin):
    return sum([int(c) for c in sbin.replace("0b", "")]) % 2
