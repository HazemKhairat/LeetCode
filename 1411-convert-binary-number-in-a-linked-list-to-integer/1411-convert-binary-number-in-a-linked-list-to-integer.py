# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        string = ""

        while head:
            string += str(head.val)
            head = head.next

        print(string)
        power = 0
        res = 0
        while string:
            res += (2**power) * int(string[-1])
            power += 1
            string = string[:-1]

        return res
