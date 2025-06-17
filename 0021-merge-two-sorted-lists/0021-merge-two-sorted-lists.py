# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        curr = head

        i = list1
        j = list2

        while i and j:
            if i.val <= j.val:
                curr.next = ListNode(i.val)
                curr = curr.next
                i = i.next
            else:
                curr.next = ListNode(j.val)
                curr = curr.next
                j = j.next
        
        while i:
            curr.next = ListNode(i.val)
            curr = curr.next
            i = i.next
        
        while j:
            curr.next = ListNode(j.val)
            curr = curr.next
            j = j.next
        
        return head.next

