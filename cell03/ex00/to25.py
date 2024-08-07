#!/usr/bin/env python3
num = int(input("Enter a First number: "))
if num > 25:
    print('Error')
while num < 26:
  print('Inside the loop, my variable is ', num)
  num += 1