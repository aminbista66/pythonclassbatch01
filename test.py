car1 = {
    "brand": "Ford",
    "model": "Mustang",
    "color": "red",
    "engine": {
        "valve": "4",
        "parts": []
    }
}

car2 = {
    "brand": "Bmw",
    "model": "X5",
    "color": "black",
    "engine": "V6"
}


class Car:
    def __init__(self, name, model, color, engine):
        print("The __init__ method was called")
        self.name = name
        self.model = model
        self.color = color
        self.engine = engine

    def display(self):
        print(f"Name: {self.name}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Engine: {self.engine}")

obj1 = Car("Ford", "Mustang", "red", "V6")
obj2 = Car("Bmw", "X5", "black", "V8")

obj1.display()
obj2.display()