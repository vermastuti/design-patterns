class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        print("Starting a Circle with radius:", radius)
    
    def draw(self):
        print("Drawing a Circle")

class Square(Shape):
    def draw(self):
        print("Drawing a Square")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a Rectangle")

class Triangle(Shape):
    def __init__(self, base):
        self.base = base
        print("Starting a Triangle with base:", base)
    
    def draw(self):
        print("Drawing a Rectangle with base:", self.base)

class FactoryDesignPattern:
    """
    Factory Design Pattern
    """

    def __init__(self):
        self._creators = {
            "Circle": Circle,
            "Square": Square,
            "Rectangle": Rectangle,
        }

    def create(self, creator_type, *args, **kwargs):
        if creator_type not in self._creators:
            raise ValueError(f"Unknown creator type: {creator_type}")
        return self._creators[creator_type](*args, **kwargs)

    def register_creator(self, creator_type, creator):
        self._creators[creator_type] = creator

    def get_creators(self):
        return self._creators

# Example usage
if __name__ == "__main__":

    factory = FactoryDesignPattern()

    # Register a creator
    factory.register_creator("Triangle", Triangle)

    # Create an instance using the registered creator
    instance = factory.create("Circle", 5)
    print(instance)  # Output: 10


    # Create an instance using the registered creator
    instance = factory.create("Triangle", 2)
    print(instance)  # Output: 10

    # Get all registered creators
    print(factory.get_creators())  # Output: {'example': <function <lambda> at ...>}