# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]):
        st = set(nums)
        while head.val in st:
            head = head.next

        prev = head
        curr = head.next
        while curr:
            if curr.val in st:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return head
