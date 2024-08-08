#!/usr/bin/env python3
from sys import argv

def teste ():

    i = len(argv)-1
    while i > 0:
        print(argv[i])
        i -= 1

teste ()


