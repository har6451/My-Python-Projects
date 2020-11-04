# Fibonacci Sequence

print("Fibonacci Series in Python")
terms = int(input("Enter Number of Terms: "))


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    for i in range(terms):
        print(fibonacci(i))


print("The Series is:")
main()
