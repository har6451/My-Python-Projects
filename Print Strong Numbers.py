# Print Strong Numbers

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


def main():
    lower = int(input("Enter Lower: "))
    upper = int(input("Enter Upper: "))
    for i in range(lower, upper + 1):
        if strong(i):
            print(i)


print("Printing Strong Numbers:")
while True:
    main()
