import time
from Shop import Shop
from Customer import Customer

DEFAULT_RUNS = 10
DEFAULT_PIZZA = "Cheese"
DEFAULT_COMPLAINT = "The pizza is too cold."


def execute_scenario():
    """Run a single customer interaction."""
    shop = Shop()
    customer = Customer(shop)

    customer.order_pizza(DEFAULT_PIZZA)
    customer.complain(DEFAULT_COMPLAINT)


def measure_execution_time(runs: int = DEFAULT_RUNS) -> float:
    """
    Measure the average execution time of the customer scenario.

    Args:
        runs: Number of benchmark iterations.

    Returns:
        Average execution time in seconds.
    """
    if runs <= 0:
        raise ValueError("runs must be greater than zero")

    total_time = 0.0

    for _ in range(runs):
        start = time.perf_counter()

        execute_scenario()

        end = time.perf_counter()
        total_time += (end - start)

    return total_time / runs


def main():
    average_time = measure_execution_time()
    print(f"Average execution time: {average_time:.8f} seconds")


if __name__ == "__main__":
    main()