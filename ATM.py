"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with assignment info.
[ ] 2. ATM runs in a "while True" loop to remain awake.
[ ] 3. Main menu uses match-case logic for selections.
[ ] 4. Inputs are validated (e.g., .isdigit()) to prevent crashes (include try except)
[ ] 5. Logic prevents overdrafts and negative deposits.
[ ] 6. All currency is formatted to two decimal places (:.2f).
[ ] 7. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

balance = 1000.00
# display menu
while True:
    print("\n Bank Menu")
    print(f"1. Balance")
    print(f"2. Deposit")
    print(f"3. Withdraw")
    print(f"4. Transfer")
    print(f"5. Exit")
    # get user choice
    choice = int(input("Please select an option (1-5): "))
    # balance
    match choice:
        case 1:
            print(f"Your balance is: ${balance:.2f}")
        # deposit
        case 2:
            try:
                deposit = float(input("Please enter desired deposit: $"))

                if deposit > 0:
                    balance += deposit
                    print(f"Deposited: ${deposit:.2f}")
                    print(f"New balance: ${balance:.2f}")
                else:
                    print("Deposit must be greater than $0")
            except ValueError:
                print("Please enter a valid number")
        # withdraw
        case 3:
            try:
                withdraw = float(input("Please enter withdrawal amount: $"))

                if withdraw <= 0:
                    print(f"Withdraw must be greater than $0")
                elif withdraw > balance:
                    print(f"Error: Insufficient funds")
                else:
                    balance -= withdraw
                    print(f"withdrew: ${withdraw:.2f}")
                    print(f"New balance: ${balance:.2f}")
            except ValueError:
                print("Please enter a valid number")
        # Transfer
        case 4:
            try:
                recipient = input("Please enter the recipients full name: ")

                transfer = float(input("Please enter transfer amount: $"))
                if transfer <= 0:
                    print(f"Transfer must be greater than $0")
                elif transfer > balance:
                    print(f"Error:Insufficient funds")
                else:
                    balance -= transfer
                    print(f"Transfer: ${transfer:.2f} to {recipient}")
                    print(f"New balance: ${balance:.2f}")
            except ValueError:
                print("Please enter a valid number")
        # exit
        case 5:
            print("Thank you for banking with us!")
            print("Goodbye.")
            break
