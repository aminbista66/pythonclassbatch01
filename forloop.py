number = int(input("Enter a number: "))

counter = 1
result = 0

while counter <= number:
    result += counter
    counter += 1

print(result)



# factorial of a number

result = 0
for i in range(1, number + 1):
    result += i

print(result)

