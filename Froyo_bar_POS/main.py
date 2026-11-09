"""
Splitting program up
"""

import os
import datetime
import employees
import orders
import print_orders
import read_menu


def clear_screen():
    _ = os.system("cls" if os.name == "nt" else "clear")


def main():
    clear_screen()

    print("Welcome to the Froyo Bar!")
    emp_id = employees.get_employee()
    order_num = orders.get_order(emp_id)

    if order_num is not None:
        orders.confirm_order(order_num)
        print_orders.print_label(order_num, emp_id)


if __name__ == "__main__":
    main()
