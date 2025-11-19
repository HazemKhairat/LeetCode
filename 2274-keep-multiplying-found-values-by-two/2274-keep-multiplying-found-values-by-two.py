class Solution:
    def findFinalValue(self, nums: List[int], org: int) -> int:
        st = set(nums)
        while org in st:
            org *= 2
        return org
