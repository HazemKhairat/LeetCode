# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        res = []
        for i in range(1, len(arr) - 1):
            if (arr[i + 1] < arr[i] > arr[i - 1]) or (arr[i + 1] > arr[i] < arr[i - 1]):
                res.append(i)

        if len(res) < 2:
            return [-1, -1]

        res.sort()
        ans = [inf, -inf]

        ans[1] = res[-1] - res[0]
        for i in range(1, len(res)):
            ans[0] = min(ans[0], res[i] - res[i - 1])
            
        return ans
