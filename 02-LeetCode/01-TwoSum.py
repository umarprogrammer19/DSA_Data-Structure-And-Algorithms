# 1. Two Sum (1st Of Jan 2025) -> Brute Force Algorithm

# Algorithm Type: Exhaustive Search

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# Solution

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


solution = Solution()
print(solution.twoSum(nums=[2, 7, 11, 15], target=9))  # [0, 1]
print(solution.twoSum(nums=[3, 2, 4], target=6))  # [1, 2]
print(solution.twoSum(nums=[3, 3], target=6))  # [0, 1]

# Explanation

# There is a function called twoSum which takes two parameters: nums and target.
# The Solution class is provided by default as boilerplate code in LeetCode. Inside this class, there is one method called twoSum.
# In the twoSum method, I use two loops. The outer loop uses the variable i and iterates through the array starting from index 0. The inner loop uses the variable j and starts from i + 1, so the same element is not used twice.

# Inside the inner loop, I check a condition:
# if nums[i] + nums[j] is equal to the target, then I return the indices [i, j].
# This way, the function finds and returns the indices of the two numbers whose sum is equal to the target.

# Example

# Input: nums = [2, 7, 11, 15], target = 9

# First, i = 0, so nums[i] = 2 -> because index 0 has value which is 2 
# Then j = 1, so nums[j] = 7 -> because index 1 has value which is 7
# nums[0] + nums[1] = 2 + 7 = 9, which is equal to the target
# Therefore, the function returns [0, 1]

# Time Complexity: O(n²)