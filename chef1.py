from dataclasses import dataclass
from Pizza import Pizza


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
    size: str
    crust_type: str
    toppings: list
    extra_cheese: bool = False
    discount_code: str = ""


class NotificationService:

    @staticmethod
    def notify(message):
        print(message)


class PricingService:

    @staticmethod
    def apply_discount(code):
        if code:
            print(f"Applying discount code: {code}")

    @staticmethod
    def apply_loyalty_points():
        print("Applying loyalty points")


class Chef:

    def __init__(self):
        self.pizza = None
        self.busy = False
        self.completed_orders = 0
        self.breaks_taken = 0
        self.kitchen_clean = True
        self.contact = ContactInfo()

    def bake_pizza(self, pizza_type):
        print(f"Chef is baking {pizza_type} pizza.")
        self.pizza = Pizza("Unknown", "Unknown", pizza_type)
        self.cut_pizza()

    def cut_pizza(self):
        print(f"Cutting {self.pizza.topping} pizza.")
        self.box_pizza()

    def box_pizza(self):
        print("Putting pizza into the box.")

    def deliver_pizza(self):
        print("Delivering pizza to cashier.")

    def hurry_up(self):
        print("Chef is hurrying up.")

    def clean_kitchen(self):
        print("Cleaning kitchen.")
        self.kitchen_clean = True

    def update_contact(self, contact: ContactInfo):
        self.contact = contact

    def process_order(self, order: Order):
        self.bake_pizza(order.pizza_type)
        PricingService.apply_discount(order.discount_code)
        self.deliver_pizza()

    def repeat_order(self, pizza_type, quantity):
        for _ in range(quantity):
            self.bake_pizza(pizza_type)

    def notify_customer(self, message):
        NotificationService.notify(message)

    def handle_complaint(self, complaint):
        handlers = {
            "cold pizza": self.clean_kitchen,
            "late delivery": self.clean_kitchen,
            "wrong order": self.clean_kitchen
        }

        handlers.get(complaint, self.clean_kitchen)()

    def perform_task(self):
        print("Real method doing the actual work")

    def is_busy(self):
        return self.busy

    def get_current_pizza(self):
        return self.pizza

    def prepare_complete_order(self, order):
        self.process_order(order)
        PricingService.apply_loyalty_points()
        self.notify_customer("Order completed.")