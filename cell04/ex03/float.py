#!/usr/bin/env python3

def main():
	try:
		number = float(input("Give me a number: "))
		number_in_string = str(number)
		dot_position = number_in_string.find(".")
		if (number_in_string[dot_position:]) != '.0':
			print("This number is a decimal.")
		else:
			print("This number is an integer.")
	except ValueError:
		print("Error")
	

if __name__ == "__main__":
	main()

"""
Para entender a linha 8
Se temos o número abaixo:

num = "32.657"

num[0] = 3 - Significa que vai pegar o conteído para posição 0
num[-1]= 7 - Signitifca que vai pegar o conteúdo da ultima posição
num[0:2] = 32. - Significa que vai pegar p conteúdo da posição 0 a 2
num[0:] = 32.657 - Significa que vai pegar tudo a partir da posição 0. 

No caso da linha 8, ele vai verificar tudo a partir do ponto (dot_position) até o final e é diferente de .0, se sim é decimal, senão é inteiro. 
Isso pelo fato de estar utilizando o [:].

"""