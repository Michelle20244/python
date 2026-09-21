"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""

seats = list(range(1, 21))

while len(seats) > 0:
    # avaliable seats
    print("Available seats")
    print(seats)

    try:
        # input
        selection = int(input("Please choose your desired seat (1-21 ): "))
        print(f"If desired to quit press 0")
        # quit
        if selection == 0:
            print("Come back soon!")
            break
        # availability
        if selection in seats:
            seats.remove(selection)
            print(f"Seat {selection} is taken.")
        else:
            print("Unavailable selection")
    except ValueError:
        print("Please input a valid number")
if len(seats) == 0:
    print("\n Unavailable seats at this time!")
