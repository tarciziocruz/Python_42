#!/usr/bin/env python3
num1 = int(input("Enter a First number: "))
num2 = int(input("Enter a Second number: "))
result = num1 * num2
print(str(num1), 'X', str(num2), '=', str(result)) 
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")