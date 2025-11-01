# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        st = set(nums)
        while head.val in st:
            head = head.next

        prev = curr = head
        while curr:
            curr = curr.next
            while curr and curr.val in st:
                curr = curr.next
            prev.next = curr
            prev = curr

        return head
