# Random Password Generator using Python

# Importing Libraries
import random
import string


# This function returns the password
def main():
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    password_length = int(input("Enter Password Length: "))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    return ''.join(s[0:password_length])


while True:
    print(main())
