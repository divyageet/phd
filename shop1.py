from dataclasses import dataclass
from enum import Enum

from Cashier import Cashier
from Chef import Chef
from Pizza import (
    CheesePizza,
    VeggiePizza,
    TunaPizza,
    PepperoniPizza,
)


@dataclass
class ContactInfo:
    first_name: str = ""
    last_name: str = ""
    address: str = ""
    phone_number: str = ""
    email: str = ""


class PizzaType(Enum):
    CHEESE = "Cheese"
    VEGGIE = "Veggie"
    TUNA = "Tuna"
    PEPPERONI = "Pepperoni"


class NotificationService:

    @staticmethod
    def notify(message: str):
        print(message)


class PricingService:

    @staticmethod
    def apply_discount(code=None):
        if code:
            print(f"Discount applied using code: {code}")
        else:
            print("No discount applied.")

    @staticmethod
    def apply_loyalty_points():
        print("Loyalty points applied.")


class Shop:

    def __init__(self):
        self.chef = Chef()
        self.cashier = Cashier(self.chef)
        self.contact = ContactInfo()
        self.current_pizza = None

        self._pizza_factory = {
            PizzaType.CHEESE: CheesePizza,
            PizzaType.VEGGIE: VeggiePizza,
            PizzaType.TUNA: TunaPizza,
            PizzaType.PEPPERONI: PepperoniPizza,
        }

    # ------------------------
    # Pizza Factory
    # ------------------------

    def create_pizza(self, pizza_type: PizzaType):
        try:
            return self._pizza_factory[pizza_type]()
        except KeyError:
            raise ValueError(f"Unsupported pizza type: {pizza_type}")

    # ------------------------
    # Order Processing
    # ------------------------

    def receive_order(self, pizza_type: PizzaType):
        print(f"Received order for {pizza_type.value} pizza.")

        self.current_pizza = self.create_pizza(pizza_type)
        self.cashier.take_order(pizza_type.value)

    # ------------------------
    # Customer
    # ------------------------

    def update_contact(self, contact: ContactInfo):
        self.contact = contact

    # ------------------------
    # Notifications
    # ------------------------

    def notify_customer(self, message):
        NotificationService.notify(message)

    # ------------------------
    # Pricing
    # ------------------------

    def apply_discount(self, code=None):
        PricingService.apply_discount(code)

    def apply_loyalty_points(self):
        PricingService.apply_loyalty_points()

    # ------------------------
    # Complaints
    # ------------------------

    def handle_customer_complaint(self, complaint):

        handlers = {
            "cold pizza": self.cashier.calm_customer_down,
            "late delivery": self.cashier.calm_customer_down,
            "wrong order": self.cashier.calm_customer_down,
        }

        handlers.get(
            complaint,
            self.cashier.calm_customer_down,
        )()

    # ------------------------
    # Shop Status
    # ------------------------

    def is_busy(self):
        return self.chef.busy

    def clean_kitchen(self):
        self.chef.clean_kitchen()

    # ------------------------
    # Workflow
    # ------------------------

    def process_order(
            self,
            pizza_type: PizzaType,
            customer: ContactInfo,
            discount_code=None,
    ):
        self.update_contact(customer)
        self.receive_order(pizza_type)
        self.apply_discount(discount_code)
        self.apply_loyalty_points()

        self.notify_customer("Order completed successfully.")