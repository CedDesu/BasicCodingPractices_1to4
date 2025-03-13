"""
range function print 0 to 100

print 0 to 100 then exclude numbers ending in zero and 5 using !=
"""

for i in range (101):
    if i % 10 != 0 and i % 10 != 5:
        print(i, end=" ")

