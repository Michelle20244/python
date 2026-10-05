"""
-----------------------------------------------------------------------
ASSIGNMENT 8A: OPTION B - EMOJI CIPHER
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. EMOJI_CIPHER constant maps every letter (A-Z) to an emoji.
[ ] 3. Program takes a word or phrase from the user.
[ ] 4. Program loops through characters and prints emojis.
[ ] 5. A 'try/except' block handles spaces or punctuation.
-----------------------------------------------------------------------
"""

EMOJI_CIPHER = {
    "A": "🍎",
    "B": "🍌",
    "C": "🐱",
    "D": "🐶",
    "E": "🥚",
    "F": "🐸",
    "G": "🍇",
    "H": "🏠",
    "I": "🍦",
    "J": "🪼",
    "K": "🔑",
    "L": "🦁",
    "M": "🌙",
    "N": "👃",
    "O": "🍊",
    "P": "🍕",
    "Q": "👑",
    "R": "🌈",
    "S": "⭐",
    "T": "🐯",
    "U": "☂️",
    "V": "🎻",
    "W": "🍉",
    "X": "❌",
    "Y": "🪀",
    "Z": "🦓",
}

while True:
    print("1. Enter English")
    print("2. Enter Coded Word")
    print("3. Quit")
    choice = input("Please select an option: ")

    if choice == "1":
        message = input("Enter English Message: ").upper()
        # TODO: Loop through each character
        for character in message:
            try:
                print(EMOJI_CIPHER[character])
            # TODO: try to print the emoji, except if it's a space or symbol
            except KeyError:
                print(character)
    elif choice == "2":
        message = input("Enter Coded Message: ").upper()
        for character in message:
            try:
                for key, value in EMOJI_CIPHER.items():
                    if character == value:
                        print(key)
            except KeyError:
                print(character)
    elif choice == "3":
        print("Goodbye")
        break