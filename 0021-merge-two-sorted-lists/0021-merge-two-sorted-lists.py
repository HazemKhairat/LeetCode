# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        i, j = list1, list2
        head = ListNode()
        curr = head
        

        while i and j:
            curr.next = ListNode()
            curr = curr.next
            if i.val <= j.val:
                curr.val = i.val
                i = i.next
            else:
                curr.val = j.val
                j = j.next

        while i:
            curr.next = ListNode()
            curr = curr.next
            curr.val = i.val
            i = i.next
            
        

        while j:
            curr.next = ListNode()
            curr = curr.next
            curr.val = j.val
            j = j.next
              
        return head.next
                