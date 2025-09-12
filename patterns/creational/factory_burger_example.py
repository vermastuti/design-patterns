# https://www.youtube.com/watch?v=dMK4TbG29fk&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=9

# used to separate creation logic from business logic; then objects would not be created and we would create objects
# Real-usage: Notification System

class Burger:

    def prepare(self):
        pass

class BasicBurger(Burger):
    def prepare(self):
        print("Preparing a basic burger with bun and patty.")

class StandardBurger(Burger):
    def prepare(self):
        print("Preparing a standard burger with lettuce, tomato, and cheese.")

class PremiumBurger(Burger):
    def prepare(self):
        print("Preparing a premium burger with desi ghee and home-made paneer")

class BasicWheatBurger(Burger):
    def prepare(self):
        print("Preparing a basic Wheat burger with bun and patty.")

class StandardWheatBurger(Burger):
    def prepare(self):
        print("Preparing a standard Wheat burger with lettuce, tomato, and cheese.")

class PremiumWheatBurger(Burger):
    def prepare(self):
        print("Preparing a premium Wheat burger with desi ghee and home-made paneer")

class Taco:
    def prepare(self):
        pass

class VeggieTaco(Taco):
    def prepare(self):
        print("Preparing a Veggie Taco")

class NonVeggieTaco(Taco):
    def prepare(self):
        print("Preparing a Non-Veggie Taco")



class BurgerFactory:

    def create_burger(self, burger_type):
        pass

    def create_taco(self, taco_type):
        pass

class SinghFactory(BurgerFactory):
    def create_burger(self, burger_type):
        if burger_type == "Basic":
            return BasicWheatBurger()
        elif burger_type == "Standard":
            return StandardWheatBurger()
        elif burger_type == "Premium":
            return PremiumWheatBurger()
        else:
            raise ValueError(f"Unkonwn burger type: {burger_type}")
        
    def create_taco(self, taco_type):
        if taco_type == "Veggie":
            return VeggieTaco()
        elif taco_type == "NonVeggie":
            return NonVeggieTaco()
        else:
            raise ValueError(f"Unknown taco type: {taco_type}")
        
class KingFactory(BurgerFactory):
    def create_burger(self, burger_type):
        if burger_type == "Basic":
            return BasicBurger()
        elif burger_type == "Standard":
            return StandardBurger()
        elif burger_type == "Premium":
            return PremiumBurger()
        else:
            raise ValueError(f"Unkonwn burger type: {burger_type}")

    def create_taco(self, taco_type):
        if taco_type == "Veggie":
            return VeggieTaco()
        elif taco_type == "NonVeggie":
            return NonVeggieTaco()
        else:
            raise ValueError(f"Unknown taco type: {taco_type}")
        

if __name__ == "__main__":
    singh_factory = SinghFactory()
    king_factory = KingFactory()

    basic_burger = singh_factory.create_burger("Basic")
    veg_taco = singh_factory.create_taco("Veggie")
    basic_burger.prepare()
    veg_taco.prepare()

    standard_burger = king_factory.create_burger("Standard")
    nonveg_taco = king_factory.create_taco("NonVeggie")
    
    standard_burger.prepare()
    nonveg_taco.prepare()

    premium_burger = singh_factory.create_burger("Premium")
    premium_burger.prepare()

