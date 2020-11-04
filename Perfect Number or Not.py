# Checking Perfect Number

def perfect_number(number):
    sum = 0
    i = 1
    while i < number:
        if number % i == 0:
            sum = sum + i
        i += 1

    if sum == number:
        return True
    else:
        return False


def main():
    num = int(input("Enter a Number: "))
    if perfect_number(num):
        print(f"{num} is a Perfect Number")
    else:
        print(f"{num} is not a Perfect Number")


print("Checking Perfect Number")
while True:
    main()
