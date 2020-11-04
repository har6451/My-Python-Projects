# Checking whether a number is Prime or Not

def prime(number):
    for i in range(2, number):
        if number % i == 0:
            return " isn't a Prime Number"
        else:
            return " is a Prime Number"
    else:
        return " isn't a Prime Number"


def main():
    print("Prime Number or Not")
    number = int(input("Enter a Number: "))
    if prime(number):
        print(str(number) + prime(number))


main()
