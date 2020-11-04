# Checking if a number is Sunny or Not
import math


def sunny(num):
    number = num + 1
    x = math.sqrt(number)
    if int(x) == x:
        return True
    else:
        return False


def main():
    num = int(input("Enter a Number: "))
    if sunny(num):
        print(f"{num} is a Sunny Number")
    else:
        print(f"{num} is not a Sunny Number")


print("Checking Sunny Number")
while True:
    main()
