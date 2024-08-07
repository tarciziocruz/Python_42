#!/usr/bin/env python3                       
entrada = input("Enter a number: ")
number = int(entrada.strip())                  #converte o valor recebido em inteiro 
if number > 0:
    print("This number is positive.")
elif number < 0:
    print("This number is negative.")
else:
    print("This number is both positive and negative.")
