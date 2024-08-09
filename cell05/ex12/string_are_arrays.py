#!/usr/bin/env python3
from sys import argv

def main ():
    size = len(argv)-1
    numz = 0
    
    if size ==1:
        for i in argv[1]:
            if i == "z":
                numz=numz+1


        if numz ==0:
            print("none")
        else:
            print(numz)
    else:
        print("none")        
        

main ()
