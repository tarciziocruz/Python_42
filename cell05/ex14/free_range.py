#!/usr/bin/env python3
from sys import argv

def main ():
    size = len(argv)
       
    if size == 3: 
        init = int(argv[1]) 
        fin =  int(argv[2])
        # array = [range(init, fin)]
        if init > fin: 
            array = list(range(init, fin-1, -1)) #essa linha se o argumento 2 for menor que o 1
        else:
            array = list(range(init, fin+1))
        print(array)
    else:
        print("none")

main ()

