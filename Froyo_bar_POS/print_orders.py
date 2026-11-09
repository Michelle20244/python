"""
import into main.
Froyo Bar POS
Prints order labels and receipts

"""

import ast


def print_label(order_nun, employee_id):
    employee = {}
    order = {}

    for key in employee:
        print(f"{key}: {employee[key]}")

    for item in order:
        print(item)

    receipt = input("Would you like a receipt (y/n)? ").strip().lower()

    if receipt == "y":
        with open("receipt.txt", "w") as f:
            for key in employee:
                f.write(f"{key}: {employee[key]}")
            for item in order:
                f.write(item)
