def get_factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    # print(f"factorial of a number: {result}")
    return result


a = int(input("Enter a number: "))
b = get_factorial(a)
print("Factorial of a number: ", b)