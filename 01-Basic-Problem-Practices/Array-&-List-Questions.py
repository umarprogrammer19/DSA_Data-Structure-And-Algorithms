# Find the maximum number in a list
def findMax(nums):
    return max(nums)


li = [1, 2, 3, 4, 101, 5, 6, 7, 8]
print(findMax(li))

# Reverse a list without using built-in functions
print(li[::-1])

# Check if a list is a palindrome
if li == li[::-1]:
    print(True)
else:
    print(False)

# Remove duplicates from a list
li = [1, 2, 3, 4, 5, 1, 1, 2, 3]
print(list(set(li)))
