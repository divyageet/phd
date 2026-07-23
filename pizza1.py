from dataclasses import dataclass
from enum import Enum


class PizzaSize(Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"


class DoughType(Enum):
    REGULAR = "Regular"
    THIN_CRUST = "Thin Crust"
    WHOLE_WHEAT = "Whole Wheat"


@dataclass
class ContactInfo:
    first_name: str = ""
    last_name: str = ""
    address: str = ""
    phone_number: str = ""
    email: str = ""


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


class Pizza:

    def __init__(
            self,
            size: PizzaSize,
            dough_type: DoughType,
            topping: str,
            extra_cheese: bool = False,
    ):
        self.size = size
        self.dough_type = dough_type
        self.topping = topping
        self.extra_cheese = extra_cheese
        self.customer = ContactInfo()

    # --------------------------
    # Customer Information
    # --------------------------

    def update_customer(self, contact: ContactInfo):
        self.customer = contact

    # --------------------------
    # Pizza Configuration
    # --------------------------

    def update_size(self, size: PizzaSize):
        self.size = size

    def update_dough(self, dough_type: DoughType):
        self.dough_type = dough_type

    def update_topping(self, topping: str):
        self.topping = topping

    # --------------------------
    # Business Logic
    # --------------------------

    def notify_customer(self, message: str):
        NotificationService.notify(message)

    def apply_discount(self, discount_code=None):
        PricingService.apply_discount(discount_code)

    def apply_loyalty_points(self):
        PricingService.apply_loyalty_points()

    def handle_complaint(self, complaint: str):
        handlers = {
            "cold pizza":
                lambda: print("Handling complaint: Pizza is cold"),
            "late delivery":
                lambda: print("Handling complaint: Pizza is late"),
            "wrong order":
                lambda: print("Handling complaint: Wrong pizza delivered"),
        }

        handlers.get(
            complaint,
            lambda: print("Handling complaint: General complaint")
        )()

    # --------------------------
    # Workflow
    # --------------------------

    def configure(self, size, dough, topping):
        self.update_size(size)
        self.update_dough(dough)
        self.update_topping(topping)

    def order(
            self,
            size,
            dough,
            topping,
            discount_code=None,
    ):
        self.configure(size, dough, topping)
        self.apply_discount(discount_code)

    def __str__(self):
        return (
            f"{self.size.value} "
            f"{self.dough_type.value} "
            f"{self.topping} Pizza"
        )


class CheesePizza(Pizza):

    def __init__(self):
        super().__init__(
            PizzaSize.MEDIUM,
            DoughType.REGULAR,
            "Cheese",
            extra_cheese=True,
        )

    def handle_complaint(self, complaint):

        if complaint == "too much cheese":
            print("Handling complaint: Too much cheese")
        else:
            super().handle_complaint(complaint)


class VeggiePizza(Pizza):

    def __init__(self):
        super().__init__(
            PizzaSize.MEDIUM,
            DoughType.WHOLE_WHEAT,
            "Veggies",
        )


class TunaPizza(Pizza):

    def __init__(self):
        super().__init__(
            PizzaSize.LARGE,
            DoughType.THIN_CRUST,
            "Tuna",
        )


class PepperoniPizza(Pizza):

    def __init__(self):
        super().__init__(
            PizzaSize.LARGE,
            DoughType.REGULAR,
            "Pepperoni",
        )