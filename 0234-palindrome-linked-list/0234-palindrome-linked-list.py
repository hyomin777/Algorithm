# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack1, stack2 = [], []

        node = head
        while node:
            stack1.append(node.val)
            node = node.next

        n = len(stack1) // 2

        for i in range(n):
            stack2.append(stack1.pop())

        if stack1[:n] == stack2:
            return True

        return False