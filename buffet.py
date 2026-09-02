"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator (Daily Specials)
DATE: [Insert Date]
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask the user for their age (convert to int) and the day of the week (convert to string).
2. Calculate the base price using if/elif/else:
   - Under 1: FREE ($0.00)
   - 1 to 11: $1.00 per year of age (Example: 5 years = $5.00)
   - 12 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. Use a match/case statement to handle special daily rules based on the day entered:
   - Tuesday: Children through age 12 are half price!
   - Sunday: Drinks are free!
   - Other days: Standard buffet pricing in effect.
4. Print the final price formatted as currency and display any applicable daily special notices.
-----------------------------------------------------------------------
"""

"""
ASSIGNMENT: 3B - The Buffet Calculator (Daily Specials)
DATE: 09/02/26
FILE: buffet.py
"""
# assigning variables
age = int(input("Please enter your age: "))
day = input("Please enter the day of the week: ")
drinks = int(input("Please enter how many drinks you will be getting: "))
# setting prices to based on age
if age < 1:
    price = 0.00
elif age <= 12:
    price = float(age)
elif age <= 64:
    price = 16.95
else:
    price = 12.95
# setting drink prices
if drinks < 1:
    drink_price = 0.00
else:
    drink_price = float(drinks)
# setting prices with specials
match day.lower():
    case "tuesday":
        if age <= 12:
            price = price / 2
            print("Tuesday Special: Children through age 12 are half price!")
    case "sunday":
        drink_price = 0.00
        print("Sunday Special: Drinks are free!")
    case _:
        print("Standard buffet pricing in effect!")
# total estimation
price = price + drink_price
print(f"Final Price: ${price:.2f}")
