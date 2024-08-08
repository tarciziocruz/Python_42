#!/usr/bin/env python3

def main():


    array = [2, 8, 9, 48, 8, 22, -12, 2]
    arraynew = []

    for i in array:
        i += 2
        arraynew.append(i)
    print (f"Original array: {array}")
    print (f" New array: {arraynew}")
    
if __name__ == "__main__":
	main()


