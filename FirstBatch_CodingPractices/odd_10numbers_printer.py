"""
ask user for 10 inputs and count odd numbers

print odd number total

"""

odd_number_input = sum(1 for _ in range(10) if int(input("Enter a number: ")) % 2 != 0)

print("The number of odd numbers is: ", odd_number_input)
