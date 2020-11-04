# Checking Spy Nature of a Number
# If the sum of all digits is equal to product of all digits, then that number is a Spy Number

def spy(number):
    sum = 0
    product = 1
    while number > 0:
        r = number % 10
        sum += r
        product *= r
        number //= 10
    if sum == product:
        return True
    else:
        return False


def main():
    num = int(input("Enter a Number: "))
    if spy(num):
        print(f"{num} is a Spy Number")
    else:
        print(f"{num} is not a Spy Number")


print("Checking Spy Nature of Number")
while True:
    main()
