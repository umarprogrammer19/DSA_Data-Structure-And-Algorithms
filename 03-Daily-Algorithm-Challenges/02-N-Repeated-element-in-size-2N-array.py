# 961. N-Repeated Element in Size 2N Array (2nd January 2026)

# You are given an integer array nums with the following properties:
# nums.length == 2 * n.
# nums contains n + 1 unique elements.
# Exactly one element of nums is repeated n times.
# Return the element that is repeated n times.

# Example 1:
# Input: nums = [1,2,3,3]
# Output: 3

# Example 2:
# Input: nums = [2,1,2,5,3,2]
# Output: 2

# Example 3:
# Input: nums = [5,1,5,2,5,3,5,4]
# Output: 5

# Constraints:

# 2 <= n <= 5000
# nums.length == 2 * n
# 0 <= nums[i] <= 104
# nums contains n + 1 unique elements and one of them is repeated exactly n times.

# Solution:

from typing import List

# Brute Force Approach

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return nums[i]


solution = Solution()
print(solution.repeatedNTimes([1, 2, 3, 3]))
print(solution.repeatedNTimes([2, 1, 2, 5, 3, 2]))
print(solution.repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]))


# Explanation
# There is a function called repeatedNTimes which takes one parameter: nums.
# The Solution class is provided by default as boilerplate code in LeetCode. Inside this class, there is one method called repeatedNTimes.

# In this method, I use two loops:
# The outer loop uses the variable i and iterates through the array starting from index 0.
# The inner loop uses the variable j and starts from i + 1, so the same element is not compared with itself.
# Inside the inner loop, I check the following condition:
# if nums[i] == nums[j]:

# If both values are equal, it means this number appears more than once in the array.
# According to the problem statement, only one number is repeated n times, so the first duplicate we find is the answer.

# As soon as a repeated number is found, the function returns that number immediately.

# Example
# Input: nums = [2, 1, 2, 5, 3, 2]

# First, i = 0, so nums[i] = 2
# Then j = 1, so nums[j] = 1 → not equal
# Next j = 2, so nums[j] = 2
# Since nums[0] == nums[2], a repeated element is found

# Therefore, the function returns: 2 because nums[i] == nums[j] is True 

# Time and Space Complexity

# Time Complexity: O(n²)
# Because two nested loops are used to compare every pair of elements.

# Space Complexity: O(1)
# No extra data structure is used.

# Hash Set Approach -> Optimized Approach Using Set 
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)


solution = Solution()
print(solution.repeatedNTimes([1, 2, 3, 3]))
print(solution.repeatedNTimes([2, 1, 2, 5, 3, 2]))
print(solution.repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]))

# Explanation
# In this approach, I use a set to keep track of elements that have already appeared in the array.
# A set is used because it allows fast lookup.

# The method works as follows:
# Create an empty set called seen
# Loop through each number in the array

# For each number:
# If it already exists in the set, it means the number is repeated, so return it
# Otherwise, add the number to the set
# Because the repeated element appears many times, it will be detected quickly.

# Example
# Input: nums = [1, 2, 3, 3]

# 1 is added to the set
# 2 is added to the set
# 3 is added to the set
# The next 3 is already in the set → repeated element found The function returns: 3  