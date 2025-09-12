# example of encapsulation

class Computer:
    def __init__(self):
        self.__maxprice = 100000 # private variable

    def buy(self):
        print(f"Buying computer for {self.__maxprice}")

    def setMaxPrice(self, price):
        self.__maxprice = price

if __name__ == "__main__":
    c = Computer()
    c.buy() # Buying computer for 100000

    # change the price
    c.__maxprice = 50000 # This will not change the actual private variable
    c.buy() # Buying computer for 100000

    # using setter function to change the price
    c.setMaxPrice(50000)
    c.buy() # Buying computer for 50000