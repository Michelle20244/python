"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with assignment title.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# Coffee shop

# Ask the user for coffee sales for two separate days
today = int(input("How many coffees were sold today?: "))
yesterday = int(input("How many coffees were sold yesterday?: "))

print(f"Coffee Shop Sales Report")
# using AND
positive = today > 0 and yesterday > 0

if positive:
    print("Congrats, you had at least one coffee sale!")
else:
    print("Unfortunately one or both days had no positive affect on sales.")

one_hundred_sales = today > 100 and yesterday > 100

if one_hundred_sales:
    print("Congrats, the coffee shop has sold over 100 coffees on both days!")
else:
    print("Unfortunately, 100 coffees were not sold on both days.")
# Using OR
even_odd = today % 2 == 0 or yesterday % 2 == 0

if even_odd:
    print("At least one day had an even number of coffee orders.")
elif even_odd:
    print("Only one day had an even number of coffee orders.")
else:
    print("Both days had an odd number of coffee orders.")

under_100 = today < 100 or yesterday < 100

if under_100:
    print("Either one of these days coffee sales were under 100.")
else:
    print("Congrats, Both sales were over 100!")
# using not
not_equal = not (today == yesterday)
if not_equal:
    print("Today's and yesterday's sales were different from each other.")
else:
    print("The exact number of coffees sold were the same on both days.")

not_zero = not (today == 0 or yesterday == 0)
if not_zero:
    print("Both days had sales!")
else:
    print("At least one of the days had zero sales.")
