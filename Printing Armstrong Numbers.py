# Printing Armstrong Numbers


def armstrong_number(number):
    temp = number
    sum = 0
    order = len(str(number))
    while number > 0:
        a = number % 10
        sum += a ** order
        number = number // 10

    if temp == sum:
        return True


def main():
    lower = int(input("Enter Lower: "))
    upper = int(input("Enter Upper: "))
    for i in range(lower, upper + 1):
        if armstrong_number(i):
            print(i)


print("Printing Armstrong Number")
while True:
    main()
