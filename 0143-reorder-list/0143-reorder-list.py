# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # finding middl (fast and slow pointer)

        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the last half

        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # reorder the linked list

        i = head
        nxt1 = i.next
        j = prev
        nxt2 = j.next

        while i and j:
            i.next = j
            i = nxt1
            if nxt1:
                nxt1 = nxt1.next
            j.next = i
            
            j = nxt2
            if nxt2:
                nxt2 = nxt2.next
            
        if i:
            i.next = None
            

        return head
