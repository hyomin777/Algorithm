# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        NewHead = None
        
        prev = None
        curr = head
        
        while curr and curr.next:
            nextPair = curr.next.next
            temp = curr.next

            curr.next = nextPair
            temp.next = curr
            
            if prev:
                prev.next = temp
            else:
                NewHead = temp  

            prev = curr
            curr = nextPair
        
        return NewHead