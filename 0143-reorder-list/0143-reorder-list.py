# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        queue = []
        node = head
        
        while node:
            queue.append(node)
            node = node.next

        node = queue.pop(0)
        cnt = 1

        while queue:
            if cnt % 2 == 0:
                val_node = queue.pop(0)
            else:
                val_node = queue.pop()

            node.next = val_node
            node = val_node
            cnt += 1
        node.next = None
