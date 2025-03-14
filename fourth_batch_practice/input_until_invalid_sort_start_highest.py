"""
initialize numbers

use while loop to ask until invalid user input

while True:
    number_input = input("Enter a number (or any non-number to stop): ")

    if not number_input.isdigit():
        print("Invalid input. Exiting program.")
        break

use numbers.sort() function to sort from lowest to highest

print number_inputs
"""

numbers = []

while True:
    number_input = input("Enter a number (or any non-number to stop): ")

    if not number_input.isdigit():
        print("Invalid input. Exiting program.")
        break

    numbers.append(int(number_input))

numbers.sort(reverse=True)

if numbers:
    print(numbers, end=" ")
else:
    print("No valid numbers were entered.")