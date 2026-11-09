import os
import datetime
import ast
import read_menu


def clear_screen():
    _ = os.system("cls" if os.name == "nt" else "clear")


def get_order(emp_id):
    menu_items = read_menu.read_menu()

    flavors, toppings, sauces, prices = read_menu.split_into_variables(menu_items)

    if not flavors or not toppings or not sauces or not prices:
        print("Check menu.txt.")
        return None

    try:
        price_per_ounce = float(prices)
    except ValueError:
        print("Invalid price in menu.txt.")
        return None

    if price_per_ounce <= 0:
        print("Price must be greater than zero.")
        return None

    clear_screen()

    # Select frozen yogurt flavor
    while True:
        list_length = read_menu.print_flavors(flavors)

        try:
            type = int(input("Enter the number for the flavor you want: ").strip())
        except ValueError:
            input(f"Enter a number (1-{list_length}). Enter to continue.")
            continue
        except Exception as e:
            right_now = datetime.datetime.now()
            with open("error.txt", "a") as f:
                f.write(f"{right_now}: {e}\n")
            continue

        if type < 1 or type > list_length:
            print(f"Enter a number (1-{list_length}).")
            continue

        flavor = flavors.split(",")[type - 1].strip()
        break

    clear_screen()

    # Select topping
    while True:
        list_length = read_menu.print_toppings(toppings)

        try:
            my_topping = int(
                input("Enter the number for the topping you want: ").strip()
            )
        except ValueError:
            print(f"Enter a number (1-{list_length}).")
            continue
        except Exception as e:
            right_now = datetime.datetime.now()
            with open("error.txt", "a") as f:
                f.write(f"{right_now}: {e}\n")
            continue

        if my_topping < 1 or my_topping > list_length:
            print(f"Enter a number (1-{list_length}).")
            continue

        topping = toppings.split(",")[my_topping - 1].strip()
        break

    clear_screen()

    # Select sauce
    while True:
        list_length = read_menu.print_sauces(sauces)

        try:
            my_sauce = int(input("Enter the number for the sauce you want: ").strip())
        except ValueError:
            print(f"Enter a number (1-{list_length}).")
            continue
        except Exception as e:
            right_now = datetime.datetime.now()
            with open("error.txt", "a") as f:
                f.write(f"{right_now}: {e}\n")
            continue

        if my_sauce < 1 or my_sauce > list_length:
            print(f"Enter a number (1-{list_length}).")
            continue

        sauce = sauces.split(",")[my_sauce - 1].strip()
        break

    clear_screen()

    # Enter ounces
    while True:
        try:
            ounces = float(input("Please enter the number of ounces: ").strip())

            if ounces <= 0:
                print("Ounces must be greater than zero.")
                continue

        except ValueError:
            print("Enter a valid number.")
            continue
        except Exception as e:
            right_now = datetime.datetime.now()
            with open("error.txt", "a") as f:
                f.write(f"{right_now}: {e}\n")
            continue

        break

    # Calculate total
    total = round(ounces * price_per_ounce, 2)

    # Store order in a dictionary
    order = {
        "employee_id": emp_id,
        "flavor": flavor,
        "topping": topping,
        "sauce": sauce,
        "ounces": ounces,
        "price_per_ounce": price_per_ounce,
        "total": total,
    }

    # Create order number
    order_num = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")

    # Append order to history
    with open("all_orders.txt", "a") as f:
        f.write(f"{order_num}:{order}\n")

    print("\nOrder saved successfully!")
    print(f"Order Number: {order_num}")
    print(f"Total: ${total:.2f}")

    return order_num


def confirm_order(order_num):
    # Read saved order from file
    order = {}

    try:
        with open("all_orders.txt", "r") as f:
            for line in f:
                parts = line.strip().split(":", 1)

    except FileNotFoundError:
        print("Order file not found.")
        return None
    except (ValueError, SyntaxError, IndexError):
        print("Error within the order.")
        return None

    if not order:
        print("Order not found.")
        return None

    while True:
        clear_screen()

        print("--- FROYO BAR ORDER REVIEW ---")
        print(f"Order Number: {order_num}\n")

        print(f"1. Flavor: {order['flavor']}")
        print(f"2. Topping: {order['topping']}")
        print(f"3. Sauce: {order['sauce']}")
        print(f"4. Ounces: {order['ounces']}")
        print(f"Total: ${order['total']:.2f}")

        correct = input("\nIs everything correct (Y/N)? ").strip().upper()

        if correct == "Y":
            return order

        if correct != "N":
            input("Enter Y or N. Press Enter to continue.")
            continue

        try:
            change = int(input("Enter the number wanted to change: ").strip())
        except ValueError:
            print("Enter a number (1-4).")
            continue
        match change:
            case 1:
                menu = read_menu.read_menu()
                flavors = menu.get("FLAVORS", "").split(",")
                for i in range(len(flavors)):
                    print(f"{i + 1}. {flavors[i].strip()}")
                try:
                    choice = int(input("New flavor number: "))
                    if choice < 1 or choice > len(flavors):
                        print("Invalid flavor number.")
                        continue
                    order["flavor"] = flavors[choice - 1].strip()
                except ValueError:
                    print("Enter a valid number.")
                    continue
            case 2:
                menu = read_menu.read_menu()
                toppings = menu.get("TOPPINGS", "").split(",")
                for i in range(len(toppings)):
                    print(f"{i + 1}. {toppings[i].strip()}")
                try:
                    choice = int(input("New topping number: "))
                    if choice < 1 or choice > len(toppings):
                        print("Invalid topping number.")
                        continue
                    order["topping"] = toppings[choice - 1].strip()
                except ValueError:
                    print("Enter a valid number.")
                    continue
            case 3:
                menu = read_menu.read_menu()
                sauces = menu.get("SAUCES", "").split(",")
                for i in range(len(sauces)):
                    print(f"{i + 1}. {sauces[i].strip()}")
                try:
                    choice = int(input("New sauce number: "))
                    if choice < 1 or choice > len(sauces):
                        print("Invalid sauce number.")
                        continue
                    order["sauce"] = sauces[choice - 1].strip()
                except ValueError:
                    print("Please enter a valid number.")
                    continue
            case 4:
                try:
                    ounces = float(input("New ounces: "))

                    if ounces <= 0:
                        print("Ounces must be greater than zero.")
                        continue

                    order["ounces"] = ounces
                except ValueError:
                    print("Please enter a valid number.")
                    continue
            case _:
                print("Choose a number 1-4.")
                continue

        # Recalculate total
        order["total"] = round(order["ounces"] * order["price_per_ounce"], 2)

        all_orders = []

        try:
            with open("all_orders.txt", "r") as f:
                all_orders = f.readlines()

            with open("all_orders.txt", "w") as f:
                for line in all_orders:
                    parts = line.strip().split(":", 1)

                    if parts[0] == str(order_num):
                        f.write(f"{order_num}:{order}\n")
                    else:
                        f.write(line)

            print("Order updated successfully!")

        except Exception as e:
            right_now = datetime.datetime.now()
            with open("error.txt", "a") as f:
                f.write(f"{right_now}: {e}\n")
            print("Could not save the updated order.")
            return None
