"""
ask user for 10 inputs and display non duplicates

use set to store first entries

for first entries:
for num in numbers:
    if num not in first_entries:
        first_entries.add(num)
        filtered_numbers.append(num)

print list of numbers
"""

numbers = [input(f"Enter number {i+1}: ") for i in range(10)]

first_entries = set()
filtered_numbers = []

for num in numbers:
    if num not in first_entries:
        first_entries.add(num)
        filtered_numbers.append(num)


print(filtered_numbers, end="")