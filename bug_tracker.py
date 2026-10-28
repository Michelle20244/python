"""
-----------------------------------------------------------------------
ASSIGNMENT 11A REVISED: THE BUG TRACKING LOG
-----------------------------------------------------------------------
[ ] 1. Program uses a while loop to keep asking for bugs.
[ ] 2. Uses the datetime module to get a timestamp format.
[ ] 3. Stores the timestamp, file name, description, and priority in a dictionary.
[ ] 4. Uses `with open("bug_log.txt", "a")` to append to the file safely.
[ ] 5. The bug_log.txt file is formatted neatly with newlines.
-----------------------------------------------------------------------
"""

import datetime


# Function in order to save bug to file
def save_to_file(timestamp_str, file_name, description, priority):
    # Store bug information
    bug_log = {timestamp_str: [file_name, description, priority]}
    # open file in append mode
    with open("bug_log.txt", "a") as file:
        file.write(f"""[{timestamp_str}])
File: {bug_log[timestamp_str][0]}
Status: {bug_log[timestamp_str][1]}
Priority: {bug_log[timestamp_str][2]}
""")


def main():
    while True:
        choice = input("Enter 'log' to record a bug, or 'quit' to stop: ")
        if choice.lower() == "log":
            # Ask user for bug information
            file_name = input("File name: ")
            description = input("Description of error: ")
            priority = input("Priority (High, Medium, Low): ")
            # current time and date
            current_time = datetime.datetime.now()
            timestamp_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
            # save info to file
            save_to_file(timestamp_str, file_name, description, priority)
            print()

        elif choice.lower() == "quit":
            print("Bug log updated.")
            break
        else:
            print("Invalid choice. Please enter 'log' or 'quit'.")


main()
