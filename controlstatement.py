# Q: display the number if the first element of the array is Even else print Not even?

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

mod = arr[0] % 2

if mod == 0:
    print(arr[0])
else:
    print("Not even")

""" user input """
# user_input = input("Enter a number: ")
# print(user_input)
# print(type(user_input))  # string

# user_input = int(user_input)  # type casting

# print(type(user_input))  # int


"""
Q: Take a user input of age and check if the age is greater than 18
    if it is then display you can go.else you cannot go

"""

# user_age = int(input("Enter your age: "))
# if user_age > 18:
#     print("You can Go")
# elif user_age > 35:
#     print("You cannot go")
# else:
#     print("You cannot Go")

# if user_age < 18 or user_age > 35:
#     print("You cannot go")
# else:
#     print("You can go")

name = "Jhon"
address = "Bharatpur"

statement = f"Your name is {name} and you live in {address} {6+1}"
# Your name is Jhon and you live in Bharatpur
print(statement)


r = float(input("Enter a radius: "))
area = 3.14*r**2

print(f"The are is", area)