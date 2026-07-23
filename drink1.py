from dataclasses import dataclass
from enum import Enum


class DrinkType(Enum):
    COKE = "Coke"
    PEPSI = "Pepsi"
    WATER = "Water"
    JUICE = "Juice"
    COFFEE = "Coffee"
    TEA = "Tea"


@dataclass(frozen=True)
class Drink:
    drink_type: DrinkType

    def create_order(self):
        print(f"Creating order for {self.drink_type.value}.")

    def add_to_order(self):
        print(f"Adding {self.drink_type.value} to the order.")

    def confirm_order(self):
        print(f"Order for {self.drink_type.value} confirmed.")

    def process_order(self):
        """Complete workflow for ordering a drink."""
        self.create_order()
        self.add_to_order()
        self.confirm_order()