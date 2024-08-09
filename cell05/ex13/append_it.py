#!/usr/bin/env python3
from sys import argv

def main ():

    size = len(argv)-1
       
    if size > 1: 
        for i in range(1, size + 1):
            if not argv[i].endswith("ism"):
                print(argv[i] + "ism")
    else:
        print("none")

main ()