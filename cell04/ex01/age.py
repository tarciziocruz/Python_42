#!/usr/bin/env python3
def main():
        try:
            age = int(input("Please tell me your age: "))
        except:
              print("Error")
              return
        print(f"You are currently {age} years old.")
        print(f"In 10 years, you'll be {age + 10} years old.")
        print(f"In 20 years, you'll be {age + 20} years old.")
        print(f"In 30 years, you'll be {age + 30} years old.")
   
if __name__ == "__main__":
	main()
