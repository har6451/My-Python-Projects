# Checking the Armstrong Number

def armstrong_number(number):
    temp = number
    r = 0
    while number > 0:
        a = number % 10
        r = r + a * a * a
        number = number // 10

    if temp == r:
        return True
    else:
        return False


def main():
    num = int(input("Enter a Number: "))
    if armstrong_number(num):
        print(f"{num} is a Armstrong Number")
    else:
        print(f"{num} is not a Armstrong Number")


print("Checking Armstrong Number")
while True:
    main()
