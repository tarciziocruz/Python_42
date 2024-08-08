#!/usr/bin/env python3
from math import ceil

def main():
	try:
		texto = str(input("Give me a text: "))
		
		print (texto.swapcase())
	except ValueError:
		print("Error")


if __name__ == "__main__":
	main()
