while True:
    name = input("Enter a name: ")
    age = input("Enter an age: ")
    gender = input("Enter gender: ")

    print(f"Name: {name}, Age: {age}, Gender: {gender}")

    data = []
    with open('data.txt', 'r') as file:
        data = file.readlines()

    data.append(f"Name: {name}\n")
    data.append(f"Age: {age}\n")
    data.append(f"Gender: {gender}\n")
    data.append("\n")

    with open('data.txt', 'w') as file:
        for line in data:
            file.write(line)

    user_input = input("Do you want to continue? (yes/no): ")
    if user_input == "yes":
        continue
    else:
        break