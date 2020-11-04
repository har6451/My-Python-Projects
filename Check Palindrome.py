# Checking whether a given string is Palindrome or not


def ispalindrome(my_string, reverse_string):
    if list(my_string) == list(reverse_string):
        print("The given string is Palindrome")
    else:
        print("The given string is not Palindrome")


def main():
    my_string = str(input("Enter a String: "))
    reverse_string = reversed(my_string)
    ispalindrome(my_string, reverse_string)


print("Checking Palindrome of a String")
while True:
    main()
