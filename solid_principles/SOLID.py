# 1. Single Responsibility Principle (SRP)
class Invoice:
    def __init__(self, items, total):
        self.items = items
        self.total = total

    def calculate_total(self):
        return sum(item['price'] * item['quantity'] for item in self.items)


class InvoicePrinter:
    def print_invoice(self, invoice):
        print("Invoice:")
        for item in invoice.items:
            print(f"{item['name']} - {item['quantity']} x {item['price']}")
        print(f"Total: {invoice.total}")


# 2. Open/Closed Principle (OCP)
from abc import ABC, abstractmethod


class Discount(ABC):
    @abstractmethod
    def apply_discount(self, total):
        pass


class NoDiscount(Discount):
    def apply_discount(self, total):
        return total


class SeasonalDiscount(Discount):
    def apply_discount(self, total):
        return total * 0.9  # 10% discount


class InvoiceWithDiscount:
    def __init__(self, total, discount: Discount):
        self.total = total
        self.discount = discount

    def get_total(self):
        return self.discount.apply_discount(self.total)


# 3. Liskov Substitution Principle (LSP)
class Bird:
    def fly(self):
        print("Flying")


class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")


class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostriches can't fly")


# 4. Interface Segregation Principle (ISP)
class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan_document(self, document):
        pass


class MultiFunctionPrinter(Printer, Scanner):
    def print_document(self, document):
        print(f"Printing: {document}")

    def scan_document(self, document):
        print(f"Scanning: {document}")


class SimplePrinter(Printer):
    def print_document(self, document):
        print(f"Printing: {document}")


# 5. Dependency Inversion Principle (DIP)
class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass


class MySQLDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to MySQL database")


class DataHandler:
    def __init__(self, database: Database):
        self.database = database

    def save_data(self, data):
        self.database.save(data)


if __name__ == "__main__":
    # SRP Example
    invoice = Invoice([{"name": "Item1", "price": 100, "quantity": 2}], 200)
    printer = InvoicePrinter()
    printer.print_invoice(invoice)

    print()

    # OCP Example
    invoice_discount = InvoiceWithDiscount(200, SeasonalDiscount())
    print(f"Total after discount: {invoice_discount.get_total()}")

    print()

    # LSP Example
    birds = [Sparrow(), Ostrich()]
    for bird in birds:
        try:
            bird.fly()
        except NotImplementedError as e:
            print(e)

    print()

    # ISP Example
    printer = SimplePrinter()
    printer.print_document("Document1")

    mfp = MultiFunctionPrinter()
    mfp.print_document("Document2")
    mfp.scan_document("Document2")

    print()

    # DIP Example
    database = MySQLDatabase()
    handler = DataHandler(database)
    handler.save_data("User data")


"""
Explanation:

Single Responsibility Principle (SRP):

Invoice handles invoice data.
InvoicePrinter handles printing the invoice.

1. Your class or method should have only one reason to change.
2. Your class or method should have only one responsibility to take care of.



Open/Closed Principle (OCP):

The Discount class is open for extension (new discount types) but closed for modification.



Liskov Substitution Principle (LSP):

Sparrow and Ostrich inherit from Bird. However, Ostrich violates LSP because it cannot fly.
Objects of a super class should be replaceable with objects of its sub classes without affecting the correctness of the program.



Interface Segregation Principle (ISP):

Separate interfaces for Printer and Scanner ensure that classes only implement what they need.
It states that no client should be forced to depend on interfaces they do not use.


Dependency Inversion Principle (DIP):

DataHandler depends on the abstraction Database, not the concrete implementation MySQLDatabase.

1. High-level modules should not depend on low-level modules. Both should depend on abstractions.
2. Abstractions should not depend on details. Details should depend on abstractions.



This code demonstrates all the SOLID principles in Python.

"""