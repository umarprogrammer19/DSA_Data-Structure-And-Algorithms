# 1975. Maximum Matrix Sum (5th Of January 2026)

# You are given an n x n integer matrix. You can do the following operation any number of times:
# Choose any two adjacent elements of matrix and multiply each of them by -1.
# Two elements are considered adjacent if and only if they share a border.
# Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

# Example 1:

# 03-Daily-Algorithm-Challenges/problemset_diagrams/05-MaxMatrixSum1.png (check the image in diagrams folder)

# Input: matrix = [[1,-1],[-1,1]]
# Output: 4
# Explanation: We can follow the following steps to reach sum equals 4:
# - Multiply the 2 elements in the first row by -1.
# - Multiply the 2 elements in the first column by -1.

# Example 2:

# 03-Daily-Algorithm-Challenges/problemset_diagrams/05-MaxMatrixSum2.png (check the image in diagrams folder)

# Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
# Output: 16
# Explanation: We can follow the following step to reach sum equals 16:
# - Multiply the 2 last elements in the second row by -1.

# Constraints:

# n == matrix.length == matrix[i].length
# 2 <= n <= 250
# -105 <= matrix[i][j] <= 105

from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        negative_count = 0
        min_abs = float("inf")

        for row in matrix:
            for val in row:
                total_sum += abs(val)

                if val < 0:
                    negative_count += 1

                min_abs = min(min_abs, abs(val))

        # If number of negatives is odd, one smallest absolute value stays negative
        if negative_count % 2 == 1:
            total_sum -= 2 * min_abs

        return total_sum


solution = Solution()
print(solution.maxMatrixSum(matrix=[[1, -1], [-1, 1]]))
print(solution.maxMatrixSum(matrix=[[1, 2, 3], [-1, -2, -3], [1, 2, 3]]))

# Logic

# Let:
# total_sum = sum of absolute values
# negative_count = count of negative numbers
# min_abs = smallest absolute value

# Case 1: Even negatives

# ✅ We can flip all negatives to positives
# ➡️ Answer = total_sum

# Case 2: Odd negatives

# ❌ One number must stay negative
# ➡️ Choose the smallest absolute value
# ➡️ Subtract 2 × min_abs

# Example 1
# matrix = [[1, -1], [-1, 1]]
# Absolute sum = 4
# Negative count = 2 (even)
# ✅ Result = 4

# Example 2
# matrix = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]
# Absolute sum = 18
# Negative count = 3 (odd)
# Smallest abs value = 1
# 18 - (2 × 1) = 16
# ✅ Result = 16

# | Type  | Complexity |
# | ----- | ---------- |
# | Time  |     O(n²)  |
# | Space |     O(1)   |
