from abc import ABC, abstractmethod

# Abstract Product A
class AbstractProductA(ABC):
    @abstractmethod
    def operation_a(self) -> str:
        pass

# Abstract Product B
class AbstractProductB(ABC):
    @abstractmethod
    def operation_b(self) -> str:
        pass

# Concrete Product A1
class ConcreteProductA1(AbstractProductA):
    def operation_a(self) -> str:
        return "ConcreteProductA1"

# Concrete Product A2
class ConcreteProductA2(AbstractProductA):
    def operation_a(self) -> str:
        return "ConcreteProductA2"

# Concrete Product B1
class ConcreteProductB1(AbstractProductB):
    def operation_b(self) -> str:
        return "ConcreteProductB1"

# Concrete Product B2
class ConcreteProductB2(AbstractProductB):
    def operation_b(self) -> str:
        return "ConcreteProductB2"

# Abstract Factory
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

# Concrete Factory 1
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()

# Concrete Factory 2
class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()

# Client Code
def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_a.operation_a()} interacts with {product_b.operation_b()}")

if __name__ == "__main__":
    print("Client: Testing with ConcreteFactory1:")
    factory1 = ConcreteFactory1()
    client_code(factory1)

    print("\nClient: Testing with ConcreteFactory2:")
    factory2 = ConcreteFactory2()
    client_code(factory2)