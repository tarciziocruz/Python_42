#!/usr/bin/env python3
from sys import argv

def main ():

    size = len(argv)-1
    i = 1
    print(f"parameters {size}")
    while i <= size:
        print(f"{argv[i]} {len(argv[i])}")
        i += 1

main ()