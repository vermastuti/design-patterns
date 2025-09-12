"""
    Decorator 'is-a' Base Class
    Decorator 'has-a' Base Class

    Decorator pattern attaches additional responsibilities to an object dynamically. 
    Decorator providea a flexible alternative to subclassing (inheritance) for extending functionality.

    Real-life usage:
        Text Editor with Bold and Italics font
        Form Validations

"""

from abc import ABC, abstractmethod

class Cake(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass


class SpongeCake(Cake):
    
    def name(self) -> str:
        return "Sponge Cake"
    
    def cost(self) -> float:
        return 300
    

class ChocolateCake(Cake):
    def name(self) -> str:
        return "Chocolate Cake"
    
    def cost(self) -> float:
        return 400


class TopCream(Cake):
    """Decorator Cream on top of cake"""
    def __init__(self, cake: Cake):
        self._cake = cake


class WhippedCream(TopCream):
    def cost(self) -> float:
        return self._cake.cost() + 100

    def name(self) -> str:
        return f"{self._cake.name()} with Whipped Cream"


class TresLeche(TopCream):
    def cost(self) -> float:
        return self._cake.cost() + 200
    
    def name(self) -> str:
        return f"{self._cake.name()} with Tres Leche"
    

if __name__ == "__main__":
    cake = SpongeCake()
    print(f"\nCost of {cake.name()} is {cake.cost()}")
    i = input("\nPress 1 for Whipped Cream \nPress 2 for Tres Leche ...\n")

    if int(i) == 1:
        cake = WhippedCream(cake)
        print(f"Cost of {cake.name()} is {cake.cost()}")
    elif int(i) == 2:
        cake = TresLeche(cake)
        print(f"Cost of {cake.name()} is {cake.cost()}")



# Component interface
# class Component(ABC):
#     @abstractmethod
#     def operation(self) -> str:
#         pass

# # Concrete Component
# class ConcreteComponent(Component):
#     def operation(self) -> str:
#         return "ConcreteComponent"

# # Base Decorator
# class Decorator(Component):
#     def __init__(self, component: Component):
#         self._component = component

#     def operation(self) -> str:
#         return self._component.operation()

# # Concrete Decorators
# class ConcreteDecoratorA(Decorator):
#     def operation(self) -> str:
#         return f"ConcreteDecoratorA({self._component.operation()})"

# class ConcreteDecoratorB(Decorator):
#     def operation(self) -> str:
#         return f"ConcreteDecoratorB({self._component.operation()})"

# # Client code
# if __name__ == "__main__":
#     # Create a simple component
#     simple = ConcreteComponent()
#     print("Client: I've got a simple component:")
#     print(f"RESULT: {simple.operation()}")

#     # Decorate the component with ConcreteDecoratorA
#     decorator1 = ConcreteDecoratorA(simple)
#     print("\nClient: Now I've got a decorated component:")
#     print(f"RESULT: {decorator1.operation()}")

#     # Further decorate the component with ConcreteDecoratorB
#     decorator2 = ConcreteDecoratorB(decorator1)
#     print("\nClient: Now I've got a doubly-decorated component:")
#     print(f"RESULT: {decorator2.operation()}")

