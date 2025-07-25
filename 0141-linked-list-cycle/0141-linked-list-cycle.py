# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        prev = curr = head

        while curr:
            curr = curr.next
            if not curr:
                return False
                
            curr = curr.next
            prev = prev.next
            if curr == prev:
                return True
        
        return False


        