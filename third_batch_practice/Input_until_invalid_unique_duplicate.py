"""
use set to store first_entries

use while loop to ask until invalid user input

while True:
    number_input = input("Enter a number (or any non-number to stop): ")

    if not number_input.isdigit():
        print("Invalid input. Exiting program.")
        break

display duplicate if input is in first_entries

else:
    print("unique")
    first_entries.add(number_input) - used to store the inputs into first_entries
"""

first_entries = set()

while True:
    number_input = input("Enter a number (or any non-number to stop): ")

    if not number_input.isdigit():
        print("Invalid input. Exiting program.")
        break

