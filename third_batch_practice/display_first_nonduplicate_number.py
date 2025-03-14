"""
ask user for 10 inputs and display non duplicates

use set to store first entries

for first entries:
for num in numbers:
    if num not in first_entry:
        first_entry.add(num)
    removed_numbers.append(num)

print list of numbers
"""

numbers = [float(input(f"Enter num_{i+1}: ")) for i in range(10)]

first_entry = set()
removed_numbers = []

for num in numbers:
    if num not in first_entry:
        first_entry.add(num)
    removed_numbers.append(num)
    pass