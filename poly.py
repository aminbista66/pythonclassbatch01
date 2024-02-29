# pol

class Vechile:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    
    def display(self):
        print(self.name)
        print(self.model)

    def move(self):
        print("Move")
        print("\n")

class Plane(Vechile):
    def move(self):
        print("Fly")
        print("\n")

        
class Boat(Vechile):
    def move(self):
        print("Sail")
        print("\n")

class Car(Vechile):

    def move(self):
        print("Drive")
        print("\n")

vechile = Vechile("Vechile", "Vechile")
vechile.display()
vechile.move()

plane = Plane("Boeing", "747")
plane.display()
plane.move()

boat = Boat("Titanic", "Titanic")
boat.display()
boat.move()

car = Car("Ford", "Mustang")
car.display()
car.move()
