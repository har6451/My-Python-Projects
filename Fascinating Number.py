# Checking Fascinating Number

# When a number( 3 digits or more ) is multiplied by 2 and 3, and
# when both these products are concatenated with the original number,
# then it results in all digits from 1 to 9 present exactly once.
# There could be any number of zeros and are ignored


def fascinating(num):
    n1 = num * 1
    n2 = num * 2
    n3 = num * 3

    my_num = str(n1) + str(n2) + str(n3)
    my_list = list(map(int, str(my_num[0:])))

    if len(set(my_list)) == len(my_list):
        return True
    else:
        return False


def main():
    num = int(input("Enter a Number: "))
    if fascinating(num):
        print(f"{num} is a Fascinating Number")
    else:
        print(f"{num} is not a Fascinating Number")


print("Checking Fascinating Number")
while True:
    main()
