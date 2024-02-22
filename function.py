def function_name(name):
    print(f"My name is {name}")

'''
Q: Given an array of integer find the count of odd and even digits
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

{
    "even": 16,
    "odd": 3
}

def find_odd_even_count(arr):
'''


def find_odd_even_count(arr):
    result = {
        "even": 0,
        "odd": 0
    }

    for i in arr:
        if i % 2 == 0:
            result["even"] += 1
        else:
            result["odd"] += 1

    print(result)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# find_odd_even_count(arr)

def fn_to_print():
    for i in range(10):
        print("Hello world")

# function_name("Jhon doe")
# fn_to_print()



'''
Q: find factorial of a number given by user
'''

def factorial(number):
    result = 1
    for i in range(1, number+1):
        result *= i            
    return result

def power(a, b):
    return a**b

fact = factorial(5)


def sum(a, b):
    return a+b

a = sum(30, 20) # 50
a = sum(10, 20) # 30

# print(a) 


person = {
    "name": "Jhon Doe",
    "age": 18,
    "address": ["Kathmandu", "Lalitpur", "Bhaktapur"]
}

# for i in person["address"]:
#     print(i)