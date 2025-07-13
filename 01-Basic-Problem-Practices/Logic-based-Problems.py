# Swap 2 variables without a third variable
a = 6
b = 8
a, b = b, a
print(a, b)

# Print multiplication table of a number.
n = int(input("Enter a number to print a table: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
