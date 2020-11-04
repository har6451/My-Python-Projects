# Checking whether a given number is Strong or Not

def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)


def strong(number):
    temp = number
    sum = 0
    while number > 0:
        r = number % 10
        sum += factorial(r)
        number //= 10

    if sum == temp:
        return True
    else:
        return False


def main():
    num = int(input("Enter a Number: "))
    if strong(num):
        print(f"{num} is a Strong Number")
    else:
        print(f"{num} is not a Strong Number")


print("Checking Strong Number")
while True:
    main()
