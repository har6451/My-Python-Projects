# Factorial using Python

def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)


def main():
    print("Factorial Using Python")
    number = int(input("Enter a Number: "))

    print(str(number) + "! = " + str(factorial(number)))


main()