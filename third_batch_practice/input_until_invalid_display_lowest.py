"""
initialize lowest

use while loop to ask until invalid user input

while True:
    number_input = (int(input("Enter a number (or any non-number to stop): "))

    if not number_input.isdigit():
        print("Invalid input. Exiting program.")
        break

use less than function and if to determine lowest number:
    if lowest is None or number < lowest:
        lowest = number_input

use if and not functions to print the lowest number
"""

lowest = None

while True:
    number_input = input("Enter a number (or any non-number to stop): ")

    if not number_input.isdigit():
        print("Invalid input. Exiting program.")
        break

    number = int(number_input)

    if lowest is None or number < lowest:
        lowest = number

if lowest is not None:
    print("Lowest number entered:", lowest)
else:
    print("No valid numbers were entered.")

