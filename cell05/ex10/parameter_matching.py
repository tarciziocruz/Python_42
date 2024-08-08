#!/usr/bin/env python3
from sys import argv

def teste ():

        parametro = input("What was the parameter? ? ")
        
        if parametro == (argv[1]):
            print('Good job!')
        else:
            print('Nope, sorry...!')
teste ()
