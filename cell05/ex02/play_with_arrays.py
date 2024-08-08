#!/usr/bin/env python3



array = [2, 8, 9, 48, 8, 22, -12, 2]
arraynew = []
size = len(array)
i = 0
while i < size:
    if array[i] > 5:
        calc = array[i] + 2
        arraynew.append(calc)
    i += 1
print (f"Original array: {array}")
print (f" New array: {arraynew}")