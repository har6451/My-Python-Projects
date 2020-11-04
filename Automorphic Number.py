# Checking Automorphic Number
# If a number is present in its square, then that number is an Automorphic Number

def automorphic(number):
    length = len(str(number))
    square = number * number
    while number > 0:
        r = square % (10 ** length)
        if r == number:
            return True
        else:
            return False


def main():
    num = int(input("Enter a Number: "))
    if automorphic(num):
        print(f"{num} is an Automorphic Number")
    else:
        print(f"{num} is not an Automorphic Number")


print("Checking Automorphic Number")
while True:
    main()
