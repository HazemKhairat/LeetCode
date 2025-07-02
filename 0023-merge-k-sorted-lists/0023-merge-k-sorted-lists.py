# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # create new list
        li = []
        # loop on the given list and for each linked-list
        # put it's elements in the new list
        for i in range(len(lists)):
            curr = lists[i]
            while curr:
                li.append(curr.val)
                curr = curr.next
        li.sort()
        
        head = ListNode()
        curr = head
        for item in li:
            curr.next = ListNode(item)
            curr = curr.next
            
        return head.next