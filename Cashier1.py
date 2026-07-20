from dataclasses import dataclass


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


class Cashier:

    def __init__(self, chef):
        self.chef = chef
        self.contact = ContactInfo()
        self.frequent_customer_discount = False

    def take_order(self, pizza_type):
        print(f"Cashier is taking order for {pizza_type} pizza.")
        self.chef.bake_pizza(pizza_type)

    def hurry_up_chef(self):
        print("Cashier is hurrying up the chef.")
        self.chef.hurry_up()

    def calm_customer_down(self):
        print("Cashier is calming the customer down.")
        self.chef.clean_kitchen()

    def deliver_pizza(self):
        print("Cashier is delivering pizza.")

    def ask_for_receipt(self):
        print("Customer is asking for a receipt.")

    # Extracted method (Long Method fixed)
    def process_order(self, pizza_type):
        self.take_order(pizza_type)
        self.deliver_pizza()
        self.ask_for_receipt()

    # Parameter Object
    def place_order(self, order: Order):
        print(
            f"Ordering {order.pizza_type} "
            f"({order.size}, {order.crust_type})"
        )
        self.take_order(order.pizza_type)

        if order.discount_code:
            self.apply_discount(order.discount_code)

        self.deliver_pizza()

    # Duplicate Code fixed
    def repeat_order(self, pizza_type, quantity):
        for _ in range(quantity):
            self.take_order(pizza_type)

    # Middle Man removed
    def perform_task(self):
        print("Real method doing the actual work")

    # Feature Envy fixed
    def check_chef_status(self):
        print(f"Chef busy: {self.chef.is_busy()}")

    # Update contact
    def update_contact(self, contact: ContactInfo):
        self.contact = contact

    def notify_customer(self, message):
        print(message)

    def apply_discount(self, discount_code):
        print(f"Applying discount: {discount_code}")

    # Duplicate conditional removed
    def handle_complaint(self, complaint):
        print(f"Complaint received: {complaint}")
        self.calm_customer_down()