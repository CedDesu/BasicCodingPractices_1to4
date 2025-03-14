"""
ask user for 10 inputs and display duplicates

use print, if and == to find duplicates
"""

numbers = [float(input(f"Enter num_{i+1}: ")) for i in range(10)]

duplicates = [value for value in numbers if numbers.count(value) != 1]

print (duplicates, end=" ")