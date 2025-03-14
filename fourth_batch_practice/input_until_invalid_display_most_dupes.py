"""
initialize numbers variable for list
numbers = []
set up while loop for input until invalid

convert input into integer

if argument to find most duplicates

if and else statement for printing the most duplicates when invalid input entered
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

    print(f"Most Duplicates: {most_frequent}")

else:
    print("No valid numbers were entered.")

