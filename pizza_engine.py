"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""

# global constants
TOPPINGS = (
    "Pepperoni",
    "Ham",
    "Sausage",
    "Bacon",
    "Cheese",
)


# functions
def making_pizza(customer, size, topping, delivered=False):
    print("\n\n---Pizza Order---")
    print(f"Customer: {customer}")
    print(f"Size: {size}")
    print(f"Topping: {topping}")
    print(f"Order will be delivered: {delivered}")

    if delivered:
        print("Estimated delivery time: 30 minutes.")
    else:
        print("Arrive to Pick-up station in 15 minutes.")
    print("Your order has been placed!")


def main():
    print("Welcome to Monty's Pizza!")
    # avaliable toppings
    print("Avaliable Toppings: ")
    for topping in TOPPINGS:
        print(topping)
    # customer info
    delivered = input("Is your order going to be delivered? (yes/no): ")
    delivered = delivered.lower() == "yes"
    customer = input("Please enter name for order: ")
    size = input("Please enter pizza size (Small, Medium, or Large): ")
    topping = input("Please choose your topping: ")

    making_pizza(
        customer=customer,
        size=size,
        topping=topping,
        delivered=delivered,
    )


main()
