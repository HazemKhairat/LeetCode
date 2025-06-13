# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li = []
        it = head

        while it:
            li.append(it.val)
            it = it.next

        if not li:
            return None
            
        newHead = ListNode(li[-1])
        curr = newHead

        for i in range(len(li) - 2, -1, -1):
            curr.next = ListNode(li[i])
            curr = curr.next
            
        
        return newHead