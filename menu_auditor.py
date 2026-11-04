"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. PHASE 1: External menu_config.txt file created in workspace.
[ ] 3. Program reads and parses the .txt file into a Dictionary.
[ ] 4. PHASE 2: break the dictionary into individual variables.
[ ] 6. Print each category and its details
[ ] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
"""


def read_menu():
    menus = {}
    try:
        with open("menu_config.txt", "r") as file:
            for line in file:
                parts_of_line = line.strip().split(":")
                category = parts_of_line[0].strip()
                detail = parts_of_line[1].strip()
                menus(category) = detail
        return menus
    except FileNotFoundError:
        print("Please make sure your txt file exists.")
        return menus
    except IndexError:
        return menus
    except Exception as e:
        print(e)
        return menus


def split_to_variables(menu_items):
    flavors = menu_items.get("FLAVORS", "")
    toppings = menu_items.get("TOPPINGS", "")
    sauces = menu_items.get("SAUCES", "")
    sizes = menu_items.get("SIZES", "")
    prices = menu_items.get("PRICES", "")
    return flavors, toppings, sauces, sizes, prices


def print_menu(flavors, toppings, sauces, sizes, prices):
    print("\n -----FROYO BAR MENU-----")

    print("\n Flavors\n")
    flavor_items = flavors.split(",")
    for item in flavor_items:
            print(f"{item.strip()}")

    print("\n Toppings\n")
    topping_items = toppings.split(",")
    for item in topping_items:
            print(f"{item.strip()}")

    print("\n Sauces\n")
    sauce_items = sauces.split(",")
    for item in sauce_items:
            print(f"{item.strip()}")

    print("\n Sizes\n")
    size_items = sizes.split(",")
    for item in size_items:
            print(f"{item.strip()}")

    print("\n Prices\n")
    price_items = prices.split(",")
    for item in price_items:
            print(f"{item.strip()}")


print("Menu Complete.")


def main():
    menu_items = read_menu()
    if menu_items:
        flavors, toppings, sauces, sizes, prices = split_to_variables(menu_items)
        print_menu(flavors, toppings, sauces, sizes, prices)


main()
