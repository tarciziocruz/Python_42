#!/usr/bin/env python3
from sys import argv

def main():
 #   argv = [[./programa],[argumento1],[argumento2],[argumento3]]

    size = len(argv)
    
    if size  < 2:
        print("none")
        return
    else:
        print(argv[1].upper())

if __name__ == "__main__":
    main()


    