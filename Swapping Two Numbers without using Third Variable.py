# Swapping of Two Variables Without Using Third Variables

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
print(f"Before Swapping: ({num1}, {num2})")


def swap(a, b):
    a = a + b
    b = a - b
    a = a - b

    return a, b


print("After Swapping: " + str(swap(num1, num2)))
