# You are designing a ride-hailing app similar to Uber or Ola and need to define a robust pricing strategy. 
# Your task is to create a detailed Low-Level Design (LLD) for the pricing system, considering the following 
# entities: Rider, Driver, Ride, and Pricing_Algorithm. Explain how your system dynamically calculates the 
# fare based on factors such as demand-supply ratio, distance, time, surge pricing, and possible discounts. 

# The design should also include how the system handles different types of rides (e.g., standard, premium, shared)
# and how it integrates with the existing ride-hailing app architecture.
# The design should be modular, scalable, and maintainable.
# The design should also consider the following:
# 1. How the system will handle surge pricing during peak hours or high demand.
# 2. How the system will calculate fares for different types of rides (e.g., standard, premium, shared).
# 3. How the system will apply discounts or promotions to the fare.
# 4. How the system will integrate with the existing ride-hailing app architecture.
# 5. How the system will handle different payment methods (e.g., credit card, cash, wallet).
# 6. How the system will handle refunds or cancellations.
# 7. How the system will handle different currencies and exchange rates.
# 8. How the system will handle different regions and their specific pricing rules.
# 9. How the system will handle different types of vehicles (e.g., sedan, SUV, bike).
# 10. How the system will handle different types of riders (e.g., new, regular, VIP).
# 12. How the system will handle different types of rides (e.g., one-way, round-trip, multi-stop).

from abc import ABC, abstractmethod

class PricingStrategy(ABC):
    @abstractmethod
    def calculate_fare(self):
        pass

class FlatPricingStrategy(PricingStrategy):
    def __init__(self):
        # super().__init__()
        self.flat_rate = 10.0  # Flat rate for the ride

    def calculate_fare(self):
        fare = self.flat_rate
        return fare
    
class SurgePricingStrategy(PricingStrategy):
    def __init__(self, distance=0, time=None):
        super().__init__()
        self.flat_rate = 20.0
        self.surge_multiplier = 1.5  # Surge pricing multiplier

    def calculate_fare(self):
        fare = self.flat_rate * self.surge_multiplier
        return fare
    

class PricingMultiplier:
    def __init__(self, strategy: PricingStrategy):
        self._strategy = strategy

    
class DemandSupplyPricingMultiplier(PricingMultiplier):
    def __init__(self, strategy: PricingStrategy):
        # super().__init__()
        self.demand_supply_ratio = 1.0  # Demand-supply ratio
        self._strategy = strategy

    def calculate_fare(self):
        # fare = (self.base_fare + (self.per_mile_rate * distance) + (self.per_minute_rate * time)) * self.demand_supply_ratio
        return self._strategy.calculate_fare() + self.demand_supply_ratio


class DistanceBasedPricingMultiplier(PricingMultiplier):
    def __init__(self, distance=5, time=None, strategy: PricingStrategy = None):
        # super().__init__()
        self.distance = distance  # Distance of the ride in miles
        self.time = time  # Time of the ride in minutes
        self.distance_rate = 1.0  # Rate per mile
        self._strategy = strategy

    def calculate_fare(self):
        # fare = (self._strategy. + self.base_fare + (self.distance_rate * distance) + (self.per_minute_rate * time))
        print(self._strategy)
        return self._strategy.calculate_fare() + (self.distance_rate * self.distance)
    

class TimeBasedPricingMultiplier(PricingMultiplier):
    def __init__(self, strategy: PricingStrategy):
        # super().__init__()
        self.time_rate = 0.5  # Rate per minute
        self.time = 10 # Time of the ride in minutes
        self._strategy = strategy

    def calculate_fare(self):
        # fare = (self.base_fare + (self.per_mile_rate * distance) + (self.time_rate * time))
        return self._strategy.calculate_fare() + (self.time_rate * self.time)

class Ride:
    def __init__(self, distance, time):
        self.distance = distance  # Distance of the ride in miles
        self.time = time  # Time of the ride in minutes
        self.fare = 0.0  # Fare for the ride
        self.pricing_strategy = FlatPricingStrategy()  # Default pricing strategy

    def set_pricing_strategy(self, strategy: PricingStrategy):
        self.pricing_strategy = strategy

    def calculate_fare(self):
        self.fare = self.pricing_strategy.calculate_fare()
        return self.fare
    
class Rider:
    def __init__(self, name):
        self.name = name  # Name of the rider
        self.rides = []  # List of rides taken by the rider

    def add_ride(self, ride: Ride):
        self.rides.append(ride)  # Add a ride to the rider's list of rides
        
    def get_total_fare(self):   
        total_fare = 0.0
        for ride in self.rides:
            total_fare += ride.calculate_fare()
        return total_fare


class Driver:   
    def __init__(self, name):
        self.name = name  # Name of the driver
        self.rides = []  # List of rides taken by the driver

    def add_ride(self, ride: Ride):
        self.rides.append(ride)  # Add a ride to the driver's list of rides

    def get_total_fare(self):
        total_fare = 0.0
        for ride in self.rides:
            total_fare += ride.calculate_fare()
        return total_fare


class RideHailingApp:
    def __init__(self):
        self.riders = []  # List of riders
        self.drivers = []  # List of drivers

    def add_rider(self, rider: Rider):
        self.riders.append(rider)  # Add a rider to the app

    def add_driver(self, driver: Driver):
        self.drivers.append(driver)  # Add a driver to the app

    def get_total_fare(self):
        total_fare = 0.0
        for rider in self.riders:
            total_fare += rider.get_total_fare()
        return total_fare
    

if __name__ == "__main__":
    # Create a ride-hailing app
    app = RideHailingApp()

    # Create riders and drivers
    rider1 = Rider("Alice")
    rider2 = Rider("Bob")
    driver1 = Driver("Charlie")
    driver2 = Driver("David")

    # Add riders and drivers to the app
    app.add_rider(rider1)
    app.add_rider(rider2)
    app.add_driver(driver1)
    app.add_driver(driver2)

    # Create rides for the riders
    ride1 = Ride(10, 20)  # 10 miles, 20 minutes
    ride2 = Ride(5, 10)   # 5 miles, 10 minutes

    # Set pricing strategy for the rides
    ride1.set_pricing_strategy(DemandSupplyPricingMultiplier(strategy=SurgePricingStrategy()))
    ride2.set_pricing_strategy(TimeBasedPricingMultiplier(strategy=SurgePricingStrategy()))

    # Add rides to the riders
    rider1.add_ride(ride1)
    # rider2.add_ride(ride2)

    # Calculate fare for the rides
    print(f"Fare for {rider1.name}'s ride: ${ride1.calculate_fare()}")
    print(f"Fare for {rider2.name}'s ride: ${ride2.calculate_fare()}")

