# Checking Leap Year

def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def main():
    if leap_year(year):
        print(f"{year} is Leap Year.")
    else:
        print(f"{year} is not Leap Year.")


print("Checking Leap Year")
while True:
    year = int(input("Enter a Year: "))
    main()
