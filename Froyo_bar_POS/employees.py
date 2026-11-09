"""
Employee info
"""

import os
import datetime


def clear_screen():
    _ = os.system("cls" if os.name == "nt" else "clear")


def get_employee():
    while True:
        try:
            emp_id = int(input("Please enter your employee ID number: "))
            break
        except ValueError:
            print("Please enter a valid ID number containing whole numbers.")
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    position = input("Please enter your position: ")

    employee_record = {
        "first_name": first_name,
        "last_name": last_name,
        "position": position,
    }

    emp_id = confirm_employee(emp_id, employee_record)

    with open("employees.txt", "a") as f:
        f.write(f"{emp_id}:{employee_record}\n")

    return emp_id


def confirm_employee(employee_id, employee_record):
    while True:
        clear_screen()

        print("Froyo Bar Employee Information\n")
        print(f"1. Employee ID:  {employee_id}")
        print(f"2. First Name: {employee_record ['first_name']}")
        print(f"3. Last name: {employee_record ['last_name']}")
        print(f"4. Position: {employee_record ['position']}")

        correct = input("Is information above correct? Y/N ").strip().upper()

        if correct == "Y":
            break
        if correct == "N":
            print("Please enter Y or N.")
            continue

        try:
            change = int(input("Please Enter (1-4) to change: "))
        except ValueError:
            print("Please enter a number (1-4).")
            continue
        match change:
            case 1:
                try:
                    employee_id = int(input("New employee ID: "))
                except ValueError:
                    print("Please enter a valid ID number containing whole numbers.")
            case 2:
                employee_record["first_name"] = input("New first name: ")
            case 3:
                employee_record["last_name"] = input("New last name: ")
            case 4:
                employee_record["position"] = input("New position: ")
            case _:
                print("Please choose from (1-4): ")
        return employee_id
