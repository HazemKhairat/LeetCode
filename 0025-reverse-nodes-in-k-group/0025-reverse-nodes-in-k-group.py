# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        parent = []

        curr = head
        while curr:
            tmp = k
            child = []
            while curr and tmp:
                child.append(curr.val)
                curr = curr.next
                tmp -= 1
            if len(child) == k:
                child.reverse()
            parent.append(child)

        res = ListNode()
        curr = res

        for child in parent:
            n = len(child)
            for i in range(n):
                curr.next = ListNode(child[i])
                curr = curr.next

        return res.next
