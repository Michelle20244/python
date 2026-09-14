"""
Error checking data entry with while statements
"""

# Name check
# Rules - can't be empty
# less than 30 characters
# should have first letter capitalized (we handle)

"""
while not fname:
    fname = input("Please enter your first name:  ")
    print(f"before: {fname}")
    fn_length = len(fname)
    print(f"length before: {fn_length}")
    fname = fname.strip()
    print(f"first name after {fname}")
    fn_length = len(fname)
    print(f"length after: {fn_length}")
"""
try:
    fname = ""
    while not fname:
        fname = input("Please enter your first name:  ")
    fname = fname.strip()

    age = -1
    while age <= 0:
        age = int(input("Please enter your child's age: (whole years, round down)"))

except ValueError:
    print(" I'm sorry, that is not a valid value")
except Exception as e:
    print(f"Error: {e}")
