# Dataclasses are a shorter way to create classes that mainly store data.
# Python automatically creates useful methods such as __init__, __repr__,
# and __eq__ for us.
#
# Compare this with classes.py: there, we wrote __init__ and __repr__ by hand.

# This lesson file is also named dataclasses.py. Remove its folder briefly so
# Python imports the standard-library dataclasses module instead of this file.
import os
import sys

lesson_folder = os.path.dirname(__file__)
sys.path.pop(0)
try:
    from dataclasses import dataclass, field
finally:
    sys.path.insert(0, lesson_folder)


@dataclass
class Product:
    # These annotations describe the data stored by every Product object.
    # The generated __init__ lets us write Product(name, price, tags).
    name: str
    price: float

    # default_factory creates a new list for every Product.
    # Without it, different products could accidentally share one list.
    tags: list[str] = field(default_factory=list)

    def discounted_price(self, percentage):
        """Return the price after applying a percentage discount."""
        return self.price * (1 - percentage / 100)


# Create an object by passing values for the fields.
product = Product("Keyboard", 80.0)
product.tags.append("hardware")
print("Product:", product)
print("Discounted price:", product.discounted_price(10))

# Dataclasses provide a useful representation and compare field values.
same_product = Product("Keyboard", 80.0, ["hardware"])
print("Products equal:", product == same_product)

# Each product receives its own independent tags list.
other_product = Product("Mouse", 25.0)
other_product.tags.append("accessory")
print("Other product:", other_product)
print("First product tags:", product.tags)
print("Other product tags:", other_product.tags)


