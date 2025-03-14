"""
initialize highest

use while loop to ask until invalid user input

while True:
    number_input = (int(input("Enter a number (or any non-number to stop): "))

    if not number_input.isdigit():
        print("Invalid input. Exiting program.")
        break

use greater than function and if to determine highest number:
    if highest is None or number < highest:
        highest = number_input

use if and not functions to print the highest number
"""

highest = None

while True:
    number_input = input("Enter a number (or any non-number to stop): ")

    if not number_input.isdigit():
        print("Invalid input. Exiting program.")
        break

    number = int(number_input)

    if highest is None or number > highest:
        highest = number

if highest is not None:
    print("Highest number entered:", highest)
else:
    print("No valid numbers were entered.")
