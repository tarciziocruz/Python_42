#!/usr/bin/env python3
def main():
        try:
            num1 = int(input("Give me the first number: "))
            num2 = int(input("Give me the second number: "))
        except:
              print("Digite somente número.")
              return
        print("Thank You!")
        print(f"{num1} + {num2} = {num1+num2}")
        print(f"{num1} - {num2} = {num1-num2}")
        print(f"{num1} / {num2} = {num1//num2}")
        print(f"{num1} * {num2} = {num1*num2}")

if __name__ == "__main__":
	main()
