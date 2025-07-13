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

# Find the second largest number in a list
arr = [10, 20, 4, 45, 99, 99]
unique = list(set(arr))
unique.sort()
second_largest = unique[-2]
print("Second largest:", second_largest)

# Move all zeros to the end of the list
li = [1, 2, 3, 4, 0, 5, 6, 7, 8, 0, 9, 0, 11]


def setZeroAtEnd(nums):
    return sorted(nums, reverse=True)


print(setZeroAtEnd(li))


# Find the common elements in two lists
def find_common(l1, l2):
    s1, s2 = set(l1), set(l2)
    return s1.intersection(s2)


same = list(find_common([1, 2, 3, 4], [3, 4, 55, 6, 1]))
print(same)


# Check if two lists have the same elements (regardless of order)
from collections import Counter

list1 = [1, 2, 2, 3]
list2 = [3, 2, 1, 2]

are_equal = Counter(list1) == Counter(list2)
print(are_equal)  # True
