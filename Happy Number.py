# Checking if a Number is Happy Number or Not
# a happy number is a number which eventually reaches 1 when replaced by
# the sum of the square of each digit.


def sum_square(number):
    sumsquare = 0
    while number > 0:
        sumsquare += (number % 10) * (number % 10)
        number //= 10
    return sumsquare


def happy(number):
    result = sum_square(number)
    try:
        while result != 1 and result != 4:
            result = happy(result)
    except:
        pass
    if result == 1:
        return True
    elif result == 4:
        return False


def main():
    num = int(input("Enter a Number: "))
    if happy(num):
        print(f"{num} is a Happy Number\n")
    else:
        print(f"{num} is not a Happy Number\n")


print("Checking Happy Number")
while True:
    main()
