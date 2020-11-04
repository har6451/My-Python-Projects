# Find the largest and smallest element among all

list = []
n = int(input("Number of Elements: "))
for i in range(1, n + 1):
    number = int(input("Enter Element: "))
    list.append(number)
list.sort()


def largest():
    return list[-1]


def smallest():
    return list[0]


def main():
    print("Largest Among All Entered Values:")
    print("Largest: " + str(largest()))

    print("Smallest Among All Entered Values:")
    print("Smallest: " + str(smallest()))


main()
