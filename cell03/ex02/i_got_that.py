#!/usr/bin/env python3
speak = str(input("What you gotta say? "))
aux = str('STOP') 
while speak != aux:
    speaking = str(input("I got that! Anything else? ")) 
    print(speaking)
    if speaking == aux:
        break