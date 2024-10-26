# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        previous = None
        current = head

        while current and current.next:
            next_pair = current.next.next
            temp = current.next

            current.next = next_pair
            temp.next = current

            if previous:
                previous.next = temp
            else:
                new_head = temp

            previous = current
            current = next_pair

        return new_head



        