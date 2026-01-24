# 1161. Maximum Level Sum of a Binary Tree (6th January 2026)

# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

# Example 1:
# 03-Daily-Algorithm-Challenges/problemset_diagrams/06-Maximum-Level-Sum-Of-Binary-Tree.JPG
# Input: root = [1, 7, 0, 7, -8, null, null]
# Output: 2

# Explanation:
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.

# Example 2:

# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105

# Solution:

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])

        level = 1
        max_sum = float("-inf")
        answer_level = 1

        while queue:
            level_sum = 0
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                answer_level = level

            level += 1

        return answer_level
    
# Explanation
# Approach (Level Order Traversal)

# We:
    # Traverse the tree level by level
    # Calculate the sum of nodes at each level

# Track:
    # Maximum sum seen so far
    # The level where that maximum occurred
    # Return the smallest level with the maximum sum

# Algorithm (Step-by-Step)

# Step 1: Initialize
    
# 1) Use a queue (FIFO) for BFS
# 2) Start with the root

# 3) Set:
        # level = 1
        # max_sum = -∞
        # answer_level = 1

# Step 2: BFS Traversal

# While queue is not empty:

# 1) Get number of nodes at current level (size)
# 2) Initialize level_sum = 0
# 3) Process all nodes in this level:
        # Add node value to level_sum
        # Push left and right children into queue (if they exist)

# Step 3: Compare

# If level_sum > max_sum
    # Update max_sum
    # Update answer_level

# Step 4: Move to next level
# Increment level

# Step 5: Return answer
# Return answer_level

# Example
# Tree: [1, 7, 0, 7, -8]

# Level 1 → 1
# Level 2 → 7 + 0 = 7  ✅
# Level 3 → 7 + (-8) = -1

# -> Maximum sum is 7 at level 2

# Time & Space Complexity

# 1) Time Complexity O(n) because Each node is visited exactly once
# 2) Space Complexity O(n) because Queue may store up to one full level of nodes
