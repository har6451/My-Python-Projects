# Number is Even or Odd using Python

def check(number):
    if number % 2 == 0:
        return 'Number is Even'
    else:
        return 'Number is Odd'


def main():
    print("Number is Even or Odd?")
    number = int(input("Enter a Number : "))

    if check(number):
        print(check(number))
    else:
        print(check(number))


main()
