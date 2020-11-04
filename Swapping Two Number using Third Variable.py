# Swapping Two Number Third Variables

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
print(f"Before Swapping: ({num1}, {num2})")


def swap(a, b):
    c = a
    a = b
    a = c
    return a, b


print(f"After Swapping: {swap(num1, num2)}")
