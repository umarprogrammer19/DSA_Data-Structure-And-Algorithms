# 2. Add Two Numbers (2nd January 2026)

# Approach: Simulation / Carry Method

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# 2 -> 4 -> 3
# 5 -> 6 -> 4
# ___________
# 7 -> 0 -> 8

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Explanation: 0 + 0 = 0.

# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# Solution


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


def list_to_linkedlist(arr):
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


solution = Solution()

l1 = list_to_linkedlist([2, 4, 3])
l2 = list_to_linkedlist([5, 6, 4])
print(linkedlist_to_list(solution.addTwoNumbers(l1, l2)))

l1 = list_to_linkedlist([0])
l2 = list_to_linkedlist([0])
print(linkedlist_to_list(solution.addTwoNumbers(l1, l2)))

l1 = list_to_linkedlist([9, 9, 9, 9, 9, 9, 9])
l2 = list_to_linkedlist([9, 9, 9, 9])
print(linkedlist_to_list(solution.addTwoNumbers(l1, l2)))

# Explanation Example 1 Step by Step

# l1: 2 -> 4 -> 3  (represents 342)
# l2: 5 -> 6 -> 4  (represents 465)

# Iteration 1:
#   val1 = 2, val2 = 5, carry = 0
#   total = 2+5+0 = 7
#   new node = 7, carry = 0

# Iteration 2:
#   val1 = 4, val2 = 6, carry = 0
#   total = 4+6+0 = 10
#   new node = 0, carry = 1

# Iteration 3:
#   val1 = 3, val2 = 4, carry = 1
#   total = 3+4+1 = 8
#   new node = 8, carry = 0

# Result linked list: 7 -> 0 -> 8

# Time & Space Complexity

# Time Complexity: O(max(m, n)) — we traverse both linked lists once.
# Space Complexity: O(max(m, n)) — new linked list for the result.

# This solution correctly handles carry, different lengths of linked lists, and returns a proper linked list without converting to integers (which LeetCode does not allow).