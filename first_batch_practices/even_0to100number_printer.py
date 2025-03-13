"""
range function print 0 to 100

print 0 to 100 then exclude odd by printing " "
"""

for i in range(101):
    print(i if i % 2 == 0 else " ")