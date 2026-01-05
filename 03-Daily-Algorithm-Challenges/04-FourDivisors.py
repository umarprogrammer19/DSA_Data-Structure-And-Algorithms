# 1390. Four Divisors (4th January 2026)

# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

# Example 1:

# Input: nums = [21,4,7]
# Output: 32
# Explanation:
# 21 has 4 divisors: 1, 3, 7, 21
# 4 has 3 divisors: 1, 2, 4
# 7 has 2 divisors: 1, 7
# The answer is the sum of divisors of 21 only.

# Example 2:

# Input: nums = [21,21]
# Output: 64

# Example 3:

# Input: nums = [1,2,3,4,5]
# Output: 0

# Constraints:

# 1 <= nums.length <= 104
# 1 <= nums[i] <= 105


# Solution (Divisor Counting Approach)

from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0

        for num in nums:
            count = 0
            div_sum = 0

            i = 1
            while i * i <= num:
                if num % i == 0:
                    count += 1
                    div_sum += i

                    other = num // i
                    if other != i:
                        count += 1
                        div_sum += other

                    if count > 4:
                        break
                i += 1

            if count == 4:
                total_sum += div_sum

        return total_sum


solution = Solution()

print(solution.sumFourDivisors([21, 4, 7]))
print(solution.sumFourDivisors([21, 21]))
print(solution.sumFourDivisors([1, 2, 3, 4, 5]))

# Explanation

# There is a function called sumFourDivisors which takes one parameter: nums, an array of integers.
# The goal is to find numbers in the array that have exactly four divisors and return the sum of those divisors.
# If no number has exactly four divisors, we return 0.

# Idea

# Every integer has divisors that come in pairs.
# If i divides num, then num // i is also a divisor.
# We only need to check divisors up to √num.
# As soon as the number of divisors becomes more than 4, we stop checking (optimization).
