"""
initialize numbers variable for list
numbers = []
set up while loop for input until invalid

convert input into integer

"""

numbers = []

while True:
    number_input = input("Enter a number (or any non-number to stop): ")

    if not number_input.isdigit():
        print("Invalid input. Exiting program.")
        break

    numbers.append(int(number_input))

if numbers:
    most_frequent = max(set(numbers), key=numbers.count)
    frequency = numbers.count(most_frequent)

    print(f"Number with the most duplicates: {most_frequent} (appeared {frequency} times)")
