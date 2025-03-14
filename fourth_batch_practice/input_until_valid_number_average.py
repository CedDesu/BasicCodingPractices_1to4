"""
initialize lowest

use while loop to ask until invalid user input

while True:
    number_input = (int(input("Enter a number (or any non-number to stop): "))

    if not number_input.isdigit():
        print("Invalid input. Exiting program.")
        break

use sum() to get sum of all numbers entered and use len() to count number of inputs
"""
numbers = []
while True:
    number_input = (input("Enter a number (or any non-number to stop): "))

    if not number_input.isdigit():
        print("Invalid input. Exiting program.")
        break

    numbers.append(int(number_input))

if numbers:
    average = sum(numbers) / len(numbers)
    print(average)
else:
    print("No valid numbers were entered.")
