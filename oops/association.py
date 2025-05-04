# Association Example: Aggregation
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} horsepower started.")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Aggregation: Car has an Engine

    def start(self):
        print(f"{self.brand} car is starting.")
        self.engine.start()  # Using the associated Engine object


# Association Example: Composition
class Room:
    def __init__(self, name):
        self.name = name

    def describe(self):
        print(f"This is the {self.name}.")


class House:
    def __init__(self, address):
        self.address = address
        self.rooms = []  # Composition: House owns Rooms

    def add_room(self, room_name):
        room = Room(room_name)  # Creating Room objects inside House
        self.rooms.append(room)

    def describe(self):
        print(f"House located at {self.address} has the following rooms:")
        for room in self.rooms:
            room.describe()


if __name__ == "__main__":
    # Aggregation Example
    engine = Engine(150)  # Create an Engine object
    car = Car("Toyota", engine)  # Associate Engine with Car
    car.start()
    # Output:
    # Toyota car is starting.
    # Engine with 150 horsepower started.

    print()

    # Composition Example
    house = House("123 Main Street")  # Create a House object
    house.add_room("Living Room")
    house.add_room("Bedroom")
    house.describe()
    # Output:
    # House located at 123 Main Street has the following rooms:
    # This is the Living Room.
    # This is the Bedroom.


"""
Explanation:


Aggregation:

The Car class has an Engine object as an attribute.
The Engine object is created outside the Car class and passed to it, showing a "has-a" relationship without ownership.


Composition:

The House class creates and owns Room objects.
The Room objects are created inside the House class, and their lifecycle is tied to the House object.
In this case, if the House object is destroyed, the Room objects are also destroyed, showing a strong ownership relationship.


This code demonstrates how objects of one class can be associated with objects of another class, either through aggregation or composition.
"""