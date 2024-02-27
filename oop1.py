class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def display(self):
        print(f"Name: {self.name}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")


bmw = Car("bmw", "x5", "black")
ford = Car("ford", "mustang", "red")

# bmw.display()
ford.display()