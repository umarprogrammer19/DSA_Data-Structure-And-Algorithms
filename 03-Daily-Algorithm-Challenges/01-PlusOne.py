# 66. Plus One (1st January 2026) Leet Code Challenge

# Method Name: String Conversion Method
# Algorithm Type: Simulation / Direct Conversion Approach

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

# Constraints:

# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.

# Solution

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = int("".join(map(str, digits))) + 1
        return list(map(int, str(result)))


solution = Solution()

print(solution.plusOne([1, 2, 3])) # [1, 2, 4]
print(solution.plusOne([4, 3, 2, 1]))
print(solution.plusOne([9]))

# Explanation (String Conversion Method)

# There is a function called plusOne which takes one parameter: digits.
# The digits array represents a large integer, where each element is a single digit.
# The digits are ordered from most significant to least significant.
# In this approach, I convert the array into a number, add one to it, and then convert it back into an array.

# Step-by-Step Explanation:
# result = int("".join(map(str, digits))) + 1

# map(str, digits) converts each digit into a string
# Example: [1, 2, 3] → ["1", "2", "3"]

# "".join(...) joins the strings into one number
# Example: "123"

# int(...) converts the string into an integer
# Example: 123

# + 1 increments the number by one
# Now the updated number is stored in result.

# Then return list(map(int, str(result)))
# str(result) converts the incremented number back to a string
# Example: "124"
# map(int, ...) converts each character back to an integer
# list(...) returns the final array of seperated digits -> 124 to [1, 2, 4]

# Example

# Input: digits = [1, 2, 3]
# Convert array to string → "123"
# Convert to integer → 123
# Add one → 124
# Convert back to array → [1, 2, 4]
# Therefore, Output: [1, 2, 4]

# Time and Space Complexity

# Time Complexity: O(n)
# Because the digits array is converted to and from strings.

# Space Complexity: O(n)
# Extra space is used for string and list conversions.
