a = 9


'''
Numeric Data Type:
int, float

Sequence Data Type:
str, list, tuple

Mapping Data Type:
dict

Boolean Data Type:
bool

Set Data Type:
set

None Data Type:
None

'''

number = 9
floatNumber = 9.002

'''list'''
arr = [1, 2, 3, 4, "String", 9.03, 90, 3]
print(arr)

''' tuple is a collection of elements that cannot be updated '''
tuplearr = (1, 2, 3, 4, "String", 9.03)

''' set is a collection of unique elements '''
setarr = {1, 2, 3, 4, 5, 6, 6, 5}

''' boolean data type '''
isTrue = True
isFalse = False


rollNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


''' Dictionary is a collection of key-value pairs '''
person = {
    "name": "John",
    "age": 23,
    "bloodGroup": "A+",
}

person["name"] = "Jane"

# print(person)

''' None is nothing '''
nothing = None

person = {
    "name": "Jane",
    "bloodGroup": None,
}



''' Operators '''
# Arithmetic Operators
# +, -, *, /, %, **, //
'''
+
- 
*
/ 
% -> Modulus
** -> Power 2**2 -> 4
// -> division without decimal 5/2 -> 2.5   5//2 -> 2
'''



# Comparison Operators
# > < == != 
# == is 


name1 = "Jhon"
name2 = "Jane"

# print(name1 is not name2)

'''
= -> is
! -> not
'''

''' function to check length of arr or string -> len '''

'''

Q: given an array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
update the center element to "Hello World" using len function

Ans:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

centerPos = int((len(arr)) // 2)

arr[centerPos] = "Hello World"

print(arr)
[1, 2, 3, 4, 5, "Hello World", 7, 8, 9, 10, 11]


Q: display True if the first element of the array is Even else False

'''

isEven = (arr[0] % 2) == 0
print(isEven)
