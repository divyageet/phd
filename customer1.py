from dataclasses import dataclass
from Drink import Drink


@dataclass
class ContactInfo:
    first_name: str = ""
    last_name: str = ""
    address: str = ""
    phone_number: str = ""
    email: str = ""


@dataclass
class Order:
    pizza_type: str
    size: str = "Medium"
    crust_type: str = "Regular"
    toppings: list = None
    discount_code: str = ""

    def __post_init__(self):
        if self.toppings is None:
            self.toppings = []


class Customer:

    def __init__(self, pizza_shop):
        self.pizza_shop = pizza_shop
        self.contact = ContactInfo()
        self.drink_order = Drink()

    # ------------------------
    # Pizza Ordering
    # ------------------------

    def order_pizza(self, order: Order):
        print(f"Ordering {order.pizza_type} pizza")
        self.pizza_shop.receive_order(order.pizza_type)

    def repeat_order(self, pizza_type, quantity):
        order = Order(pizza_type)

        for _ in range(quantity):
            self.order_pizza(order)

    # ------------------------
    # Complaints
    # ------------------------

    def complain(self, complaint):
        print(f"Complaint: {complaint}")

        # Delegate to PizzaShop instead of message chain
        self.pizza_shop.handle_customer_complaint(complaint)

    def handle_complaint(self, complaint):

        handlers = {
            "cold pizza": lambda: self.complain("Pizza is cold"),
            "late delivery": lambda: self.complain("Pizza is late"),
            "wrong order": lambda: self.complain("Wrong pizza delivered")
        }

        handlers.get(
            complaint,
            lambda: self.complain("General complaint")
        )()

    # ------------------------
    # Contact Information
    # ------------------------

    def update_contact(self, contact: ContactInfo):
        self.contact = contact

    # ------------------------
    # Notification
    # ------------------------

    def notify(self, message):
        print(message)

    # ------------------------
    # Discount
    # ------------------------

    def apply_discount(self, code):
        if code:
            print(f"Discount applied: {code}")

    def apply_loyalty_points(self):
        print("Loyalty points applied")

    # ------------------------
    # Drink
    # ------------------------

    def order_drink(self, drink_type):

        print(f"Ordering {drink_type}")

        self.drink_order.create_order(drink_type)
        self.drink_order.add_to_order()
        self.drink_order.confirm_order()

    # ------------------------
    # Utility
    # ------------------------

    def is_shop_busy(self):
        return self.pizza_shop.is_busy()