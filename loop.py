'''
for -> array or range

'''

# arr = [1, 3, 4, 5, 6, 7, 8, 9]

''' in operator '''
# for i in arr:
#     print(i)

''' range function '''
# for i in range(4, 8):
#     print(arr[i])


''' while function '''
# counter = 0

# while counter < len(arr):
#     if arr[counter] % 2 == 0:
#         continue
#     print(arr[counter])
#     counter += 1


'''
Q: Take a number as input and display the sum of number from 1 to that number

'''

user_input = int(input("Enter a number: "))

result = 0

for i in range(1, user_input + 1):
    result += i

print(result)



number = input("Enter a number: ")
if number % 2 == 0:
    print("Even")

while True:
    print("Even")
    
    if number % 2 == 0:
        break

    print("Odd")


rollno = [1, 2, 3, 4, 5, 6, 7,8,9]

for i in range(9):
    print(i)