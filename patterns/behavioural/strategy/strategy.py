"""
    Real-life usage: 
        Payment Strategy, Sorting Algorithms
    
    Used to vary algorithms at runtime
"""

from abc import ABC, abstractmethod

from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def initiate_payment(self, amount):
        pass


class UPIPayment(PaymentMethod):
    def initiate_payment(self, amount):
        print(f"Initiating UPI payment of {amount}")


class CreditCardPayment(PaymentMethod):
    def initiate_payment(self, amount):
        print(f"Initiating Credit Card payment of {amount}")


class CashPayment(PaymentMethod):
    def initiate_payment(self, amount):
        print(f"Initiating Cash payment of {amount}")


class PaymentContext:
    def __init__(self, payment_method: PaymentMethod):
        self._payment_method = payment_method

    def set_payment_method(self, payment_method: PaymentMethod):
        self._payment_method = payment_method

    def initiate_payment(self, amount):
        self._payment_method.initiate_payment(amount)


# Strategy Interface
class Strategy(ABC):
    @abstractmethod
    def execute(self, data):
        pass

# Concrete Strategies
class ConcreteStrategyA(Strategy):
    def execute(self, data):
        return sorted(data)

class ConcreteStrategyB(Strategy):
    def execute(self, data):
        return sorted(data, reverse=True)

class ConcreteStrategyC(Strategy):
    def execute(self, data):
        return [x * 2 for x in data]

# Context
class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, data):
        return self._strategy.execute(data)

# Example Usage
if __name__ == "__main__":
    data = [5, 2, 9, 1]

    context = Context(ConcreteStrategyA())
    print("Strategy A:", context.execute_strategy(data))

    context.set_strategy(ConcreteStrategyB())
    print("Strategy B:", context.execute_strategy(data))

    context.set_strategy(ConcreteStrategyC())
    print("Strategy C:", context.execute_strategy(data))