# -*- coding: utf-8 -*-

def countletters(str_in):
    str_in = list(str_in.lower())
    occurences = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        k = 0
        while letter in str_in:
            k = k + 1
            str_in.remove(letter)
        if k != 0:
            occurences.append([letter,k])
    occurences.sort()
    return occurences

print(countletters("a bb ccc dddd eeeee ffffff"))
