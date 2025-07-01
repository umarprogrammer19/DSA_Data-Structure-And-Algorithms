# Check if a number is even or odd.

n = int(input("Enter A Number: "))
even = "Even Number" if n % 2 == 0 else "Odd Number"
print(even)

# Find the largest of three numbers.
from functools import reduce

num2 = input("Enter 3 Numbers: ").split()
val = [int(c) for c in num2]

largest = reduce(lambda x, y: x if x > y else y, val)  # for one line answer
print(largest)

# For Normal
largest = val[0]

for value in val:
    if value > largest:
        largest = value

print(largest)
