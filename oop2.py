# inheritance / Polymorhpism
class Vechile:
    def __init__(self, vechile_number, chassis_number, category):
        self.vechile_number = vechile_number
        self.chassis_number = chassis_number
        self.category = category

    def display(self):
        print(f"Vechile Number: {self.vechile_number}")
        print(f"Chassis Number: {self.chassis_number}")
        print(f"Category: {self.category}")
    
    def say_hello(self):
        print("Hello from Vechile")

v1 = Vechile("1234", "1234", "four-wheeler")
v1.display()

class Bike(Vechile):
    def __init__(self, name, model, color, vechile_number, chassis_number):
        self.name = name
        self.model = model
        self.color = color
        super().__init__(vechile_number, chassis_number, "two-wheeler")
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        super().display()


# bike = Bike(
#     name="Kawasaki",
#     model="Zx10r",
#     color="green",
#     vechile_number="9988",
#     chassis_number="124324",
# )

# bike.display()

class ModifiedBike(Bike):
    def __init__(self, name, model, color, vechile_number, chassis_number, modifications):
        self.modifications = modifications
        super().__init__(name, model, color, vechile_number, chassis_number)

    def display(self):
        super().display()
        print(f"Modifications: {self.modifications}")


modified_bike = bike = ModifiedBike(
    name="Kawasaki",
    model="Zx10r",
    color="green",
    vechile_number="9988",
    chassis_number="124324",
    modifications=["nitro", "akrapovic", "racing clutch"]
)

modified_bike.display()



import os

os.environ.get("SECRET_KEY")