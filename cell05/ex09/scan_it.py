#!/usr/bin/env python3
from sys import argv

def teste ():

    i = len(argv)-1
    if i <= 1:
        print("none")
    else:
        print(argv[i])

teste ()