"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 5 inputs have 'while' loop validation.
[ ] 3. The more tickets loop uses .upper() and correct Boolean logic.
[ ] 4. Include a try and except statement around the entire program. Should have one defined
       exception (probably value error) and a generic exception
[ ] 5. Have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""

# First name and last name
try:
    first_name = input("Please enter your first name: ")
    while first_name == "":
        print("Error: Name cannot be blank.")
        first_name = input("Please enter first name: ")
    first_name = first_name.strip()

    last_name = input("Please enter your last name: ")

    while last_name == "":
        print("Error: Name cannot be blank")
        last_name = input("Please enter your last name: ")
    last_name = last_name.strip()

except ValueError:
    print("A value error occured.")
except Exception:
    print("An unexpected error occured.")

# age
age = 0

while age <= 0:
    try:
        age = int(input("Please enter your age: "))

        if age <= 0:
            print("Error: Please enter a valid age.")
    except ValueError:
        print("Error: Age must be numerical.")

phone_number = ""
while phone_number == "":
    phone_number = input("Please enter your phone number: ")
    if phone_number == "":
        print("Error: Phone number cannot be blank.")
phone_number = phone_number.strip()

# drink ticket?

if age >= 21:
    drink_ticket = True
    print("You shall receive a drink ticket.")
else:
    drink_ticket = False
    print("You will not receive a drink ticket.")

# ticket count

ticket_count = 0

while ticket_count <= 0:
    try:
        ticket_count = int(input("How many tickets: "))

        if ticket_count <= 0:
            print("Error: Ticket count cannot be 0.")
    except ValueError:
        print("Error: Ticket count must be rounded.")
        ticket_count = 0

# additional tickets

additional_tickets = input("Are there additional tickets?: ")

while additional_tickets != "Y" and additional_tickets != "N":
    print("Error: Please only enter values under Y or N.").upper()
    additional_tickets = input("Are there additional tickets?: ")

# registration summary
print("Registration Summary:")
print("Name:", first_name, last_name)
print("Age:", age)
print("Phone Number:", phone_number)
print("Total Tickets:", ticket_count)

if drink_ticket:
    print("Drink ticket: Yes")
else:
    print("Drink ticket: No")
