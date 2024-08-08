#!/usr/bin/env python3
from sys import argv

def main():

    size = len(argv)
    if size <2:
        print("none")
        return
    else:
        print(f"{argv[1]}")


if __name__ == "__main__":
    main()