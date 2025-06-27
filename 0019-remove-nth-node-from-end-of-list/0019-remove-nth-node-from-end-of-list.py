# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = head
        cnt = 0
        while tmp:
            cnt += 1
            tmp = tmp.next

        target = cnt - n
        if target == 0:
            return head.next

        index = 0
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            if index == target:
                curr.next = None
                prev.next = nxt
                break
            prev = curr
            curr = nxt
            index += 1

        return head
