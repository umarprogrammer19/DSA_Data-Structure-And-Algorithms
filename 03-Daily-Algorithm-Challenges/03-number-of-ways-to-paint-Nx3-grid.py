# 1411. Number of Ways to Paint N × 3 Grid (3rd January 2026)

# You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

# Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.

# Example 1:
# Input: n = 1
# Output: 12
# Explanation: There are 12 possible way to paint the grid as shown.
# Example 2:

# Input: n = 5000
# Output: 30228214


class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        a, b = 6, 6

        for _ in range(2, n + 1):
            new_a = (3 * a + 2 * b) % MOD
            new_b = (2 * a + 2 * b) % MOD
            a, b = new_a, new_b

        return (a + b) % MOD


solution = Solution()
print(solution.numOfWays(1))
print(solution.numOfWays(5000))
