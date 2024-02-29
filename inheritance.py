# inheritance / polymorphism
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def display(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print("\n")


person3 = Person("Jack", "Doe")
person3.display()


class Student(Person):
    def __init__(self, first_name, last_name, year):
        super().__init__(first_name, last_name)
        self.year = year
    
    def display(self):
        print(f"Year: {self.year}")
        super().display()

person1 = Student("John", "Doe", 2022)
person1.display()

person2 = Student("Jane", "Doe", 2023)
person2.display()




