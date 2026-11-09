"""
Will read menu information from menu.txt
"""

import os


def read_menu():
    menu = {}

    try:
        file_path = os.path.join(os.path.dirname(__file__), "menu.txt")
        with open(file_path, "r") as file:
            for line in file:
                parts_of_line = line.strip().split(":", 1)
                category = parts_of_line[0].strip()
                detail = parts_of_line[1].strip()
                menu[category] = detail

        return menu
    except FileNotFoundError:
        print('Create file or check file name ("menu.txt")')
        return menu
    except IndexError:
        print("Error within menu.txt")
        return menu
    except Exception as e:
        print(e)
        return menu


def split_into_variables(menu_items):
    flavors = menu_items.get("FLAVORS", "")
    toppings = menu_items.get("TOPPINGS", "")
    sauces = menu_items.get("SAUCES", "")
    prices = menu_items.get("PRICES", "")

    return flavors, toppings, sauces, prices


def print_flavors(flavors):
    print("\n Frozen Yogurt Flavors Available: ")
    flavor_items = flavors.split(",")
    count = 1
    for item in flavor_items:
        print(f"{count}. \t{item.strip()}")
        count += 1
    return len(flavor_items)


def print_toppings(toppings):
    print("\n Available Toppings: ")
    topping_items = toppings.split(",")
    count = 1
    for item in topping_items:
        print(f"{count}. \t{item.strip()}")
        count += 1
    return len(topping_items)


def print_sauces(sauces):
    print("\n Available Sauces: ")
    sauce_items = sauces.split(",")
    count = 1
    for item in sauce_items:
        print(f"{count}. \t{item.strip()}")
        count += 1
    return len(sauce_items)


def print_prices(prices):
    print(f"\n Price per ounce: ${float(prices):.2f}")
