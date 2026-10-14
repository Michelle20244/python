"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")


# TODO: Define get_price(size)
def get_price(size):
    match size:
        case "small":
            return 3.0
        case "medium":
            return 4.0
        case "large":
            return 5.0
        case _:
            print("invalid option.")
            return 0.0


# TODO: Define blend(size, base, fruit, scoops)
def blend(size, base, fruit, scoops):
    print("---Smoothie Order---")
    print("Base:", base)
    print("Size:", size)
    print("Fruit:", fruit)
    print("Scoops:", scoops)
    print("Price: $", format(get_price(size), ".2f"))


# TODO: Define main() to collect input and call your logic
def main():
    size = input("What size smoothie do you want (small, medium, large): ").lower()
    if size not in ("small", "medium", "large"):
        print("Invalid selection.")
        return
    print("Available Bases:", BASES)
    base = input("Selection of base: ").title()
    if base not in BASES:
        print("Invalid selection.")
        return
    print("Available Fruits:", FRUITS)
    fruit = input("Selection of fruit: ").title()
    if fruit not in FRUITS:
        print("Invalid selection.")
        return
    try:
        scoops = int(input("How many scoops of fruit would you like?"))
        if scoops <= 0:
            print("Selection must be at least 1 scoop")
            return
    except ValueError:
        print("Invalid selection. Please type number rounded to a whole number.")
        return
    price = get_price(size)
    print("Base Price: $", format(price, ".2f"))
    blend(size, base, fruit, scoops)


main()
