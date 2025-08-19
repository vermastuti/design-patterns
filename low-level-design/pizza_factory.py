
class Customer:
    def __init__(self, name):
        self.name
        self.address
        self.orders
        self.phone_number
        self.email
        self.customer_id

    def view_order_history(self): pass
    def place_order(self): pass
    def cancel_order(self): pass
    def track_order(self): pass
        

class Order:
    def __init__(self, name):
        self.order_id
        self.status
        self.customer_id
        self.payment_status
        self.payment_method
        self.items
        self.total_price
        self.order_date
        self.delivery_date
        self.delivery_address
        self.delivery_time
        self.delivery_instructions

    def check_order_status(self): pass
    def update_order_status(self): pass
    def calculate_total_price(self): pass
    def apply_discount(self): pass
    def assign_delivery(self): pass


class Pizza:
    def __init__(self):
        self.pizza_id
        self.name
        self.toppings
        self.base_price
        self.ingredients
        self.size
        self.crust_type
    
    def calculate_price(self): pass
    def add_toppings(self): pass
    def fetch_ingredients(self): pass
    def alter_crust_type(self): pass


class Topping:
    
    def __init__(self): 
        self.name
        self.topping_id
        self.price


    def is_available(self): pass
    def update_price(self): pass


class Payment:
    def __init__(self): 
        self.payment_id
        self.payment_method
        self.payment_status
        self.payment_date
        self.order_id
        self.total_amount
        self.discount_applied

    def initiate_payment(self): pass
    def refund_payment(self): pass


class Inventory:
    def __init__(self): 
        self.item_id
        self.quantity
        self.item_name

    def update_stock(self): pass
    def check_availability(self): pass


class Delivery_Executive:
    def __init__(self):
        self.name
        self.person_id
        self.phone_number
        self.identification_id
        self.rating
    
    def update_order_status(self): pass
    def pick_order(self): pass


class KitchenStaff:
    def __init__(self):
        self.name
        self.staff_id
        self.order_id
        self.role
    
    def prepare_order(self): pass
    def update_order_status(self): pass


"""
Relationships:

Customer places Order → 1-to-many
Order has Pizza → 1-to-many
Pizza includes Topping → many-to-many
Order has Payment → 1-to-1
KitchenStaff prepares Order → many-to-many (via assignments)
DeliveryExecutive delivers Order → 1-to-1
Inventory tracks Toppings and Ingredients

How to Explain:

Focus on Object Interactions:

Show how a customer placing an order leads to object creation (Order, Pizza, Payment).
 

Discuss Relationships:

Use aggregation/composition to explain has-a relationships.
 

Ideas to Extend:

Ask how to support combo offers, discount coupons, or real-time tracking
"""