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


def get_menu_options():
    menu = {}
    while True:
        print("Type 'Q' when done.")
        category = input("Give me a category: ")
        if category == "Q":
            break
        items = input("Enter items separated by commas: ")
        menu[category] = items
    return menu


def save_to_file(menu):
    # save menu with configuration
    with open("menu_config.txt", "w") as file:
        all_items = menu.items()
        for item in all_items:
            output = f"{item[0]},{item[1]}"
            file.write(output + "\n")


def main():
    # create menu and save
    my_menu = get_menu_options()
    save_to_file(my_menu)
    print("Froyo Bar menu saved!")


main()
