"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included (Copy and paste THIS comment from opening to closing quotes).
[ ] 2. Program asks for at least 5 different inputs (variables).
[ ] 3. Output uses F-Strings to combine text and variables.
[ ] 4. Output uses at least one escape sequence (\n or \t).
[ ] 5. Code contains comments explaining the steps.
[ ] 6. Program runs without errors.
-----------------------------------------------------------------------
"""

# Declare variables
name = ""
animal = ""
color = ""
# Get user input and assign to variables
name = input("Please enter a person's name: ")
animal = input("Please enter a type of animal: ")
color = input("Please enter a color: ")
food = input("Please enter a food: ")
clothing_brand = input("Please enter a clothing brand: ")
verb = input("Please enter an verb: ")
# Output
print(
    f"\tOnce upon a century time, there was a hypebeast named, {name}, who went to a park."
)
print(f"\tThere {name} saw an {animal} who was {verb}.")
print(
    f"\tThe {animal} was in a {color} {clothing_brand} sweater who had {food} in their hand."
)
print(
    f"\tWeirdly {name} and the {animal} decided to join together while {verb} and eating {food}."
)
