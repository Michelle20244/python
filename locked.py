"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE DEPARTMENT SECURITY TERMINAL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Department constant defined in ALL_CAPS.
[ ] 3. Username tuple and password list defined.
[ ] 4. While loop runs interactively.
[ ] 5. Try/except catches TypeError and tells user to email help desk.
-----------------------------------------------------------------------
"""

# list of usernames from chatgpt
User_names = (
    "michcore",
    "michluv",
    "michhxo",
    "michszn",
    "itsmichh",
    "onlymich",
    "heyymich",
    "m1chelle",
    "miche11e",
)
# list of passwords from chatgpt
pass_words = [
    "Cookie123!",
    "BlueSky45",
    "Coffee789",
    "PinkStar22!",
    "Gaming456",
    "Cyber321",
    "Laptop88!",
    "Network99",
    "Python2026!",
]

while True:
    print("1. Look up username")
    print("2. Change password")
    print("3. Change username")
    print("4. Exit")

    try:
        selection = int(input("Please enter your selection (1-4): "))
        print(User_names)
        # look up username
        if selection == 1:
            try:
                index = int(input("Please enter row of username (0-8): "))
                print("Username:", User_names[index])
                print("Password:", pass_words[index])
            except ValueError:
                print("Please enter a valid number.")
            except IndexError:
                print("That user row is not valid.")
        # update password
        elif selection == 2:
            try:
                index = int(input("Please enter row of username (0-8): "))
                new_pass_word = input("Please enter your new password: ")
                pass_words[index] = new_pass_word
                print("New password:", pass_words[index])
            except ValueError:
                print("Please enter a valid number.")
            except IndexError:
                print("That user row is not valid.")
        elif selection == 3:
            try:
                index = int(input("Please enter row of username (0-8): "))
                new_username = input("Please enter your new username: ")
                User_names[index] = new_username

            except TypeError:
                print(
                    "Usernames cannot be changed! Please email help desk for more assistance."
                )
            except ValueError:
                print("Please enter a valid number.")
            except IndexError:
                print("That user row is not valid.")
        # exit menu
        elif selection == 4:
            print("Now exiting...")
            break

    except:
        print("Please choose from 1-4")
