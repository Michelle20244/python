# GLOBAL CONSTANTS
OFFICE_NAME = "Office Hero Dashboard"
TAX_RATE = 0.05


def process_expenses(item_name, price, quantity):
    """Calculates tax and returns TWO values (total, status)."""
    subtotal = price * quantity
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    # Determine a string status based on logic
    msg = f"{quantity} {item_name} (s) purchased"
    return total, msg  # Multiple Return


def main():
    print(OFFICE_NAME)

    item_name = input("Please enter item name: ")
    try:
        user_price = float(input("Enter item price: "))
        user_quantity = int(input("Enter quantity of item: "))
    except ValueError:
        print("Invalid input. Defaulting to 1.00")
        user_price = 1.00
        user_quantity = 1

    # UNPACKING the two returned values
    final_cost, summary_txt = process_expenses(
        item_name=item_name, price=user_price, quantity=user_quantity
    )

    print(f"\nFinal Receipt: ${final_cost:.2f}")
    print(f"Total summary of purchases: {summary_txt}")


main()
