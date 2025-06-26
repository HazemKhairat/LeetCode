# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle

        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # reorder List
        h1, h2 = head, prev

        while h1 and h2:
            print(h1.val)
            print(h2.val)
            n1 = h1.next
            h1.next = h2
            h1 = n1
            n2 = h2.next
            h2.next = h1
            h2 = n2

        if h1:
            h1.next = None

        return head
