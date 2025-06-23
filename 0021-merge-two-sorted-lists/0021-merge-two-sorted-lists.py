# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        i, j = list1, list2
        head = ListNode()
        curr = head

        while i or j:
            curr.next = ListNode()
            curr = curr.next
            if (i and j and i.val <= j.val) or (i and not j):
                curr.val = i.val
                i = i.next
            elif j:
                curr.val = j.val
                j = j.next

        return head.next
