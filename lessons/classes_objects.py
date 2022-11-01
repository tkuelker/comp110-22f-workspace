"""Example of a class and object instantiation."""


class Pizza:
    """Models the idea of a Pizza."""

    extra_cheese: bool

    def __init__(self, size: str, toppings: int):
        """Constructor definition for initialization of attributes."""
        self.size = size
        self.toppings = toppings

    def price(self, tax: float) -> float:
        """Calculate the price of a Pizza."""
        total: float = 0.0
        if self.size == "large":
            total += 10.0
        else:
            total += 8.0

        total += self.toppings * .75

        if self.extra_cheese:
            total += 1.0

        total *= tax

        return total


a_pizza: Pizza = Pizza("large", 3)
print(f"Price: ${a_pizza.price(1.05)}")

another_pizza: Pizza = Pizza("small", 0)
another_pizza.extra_cheese = True
print(f"Price: ${another_pizza.price(1.05)}")