"""
ask user for 10 inputs and count even numbers

print odd number total

"""

even_number_input = sum(1 for _ in range(10) if int(input("Enter a number: ")) % 2 == 0)

print("The number of even numbers is: ", even_number_input)