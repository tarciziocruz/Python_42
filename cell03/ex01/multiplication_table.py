#!/usr/bin/env python3
num = int(input("Enter a number: "))
print(num)
aux = 0
while aux <=10:
    mult = num * aux
    print(aux, 'X', num, '=', mult)
    aux = aux + 1 
