"""
ask user for 10 inputs and display non duplicates

use print, if and == to find non duplicates
"""

numbers = [float(input(f"Enter num_{i+1}: ")) for i in range(10)]

non_duplicates = [value for value in numbers if numbers.count(value) == 1]

print (non_duplicates, end=" ")