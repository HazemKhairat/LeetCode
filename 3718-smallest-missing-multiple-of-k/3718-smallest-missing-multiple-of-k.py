class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        st = set(nums)
        ans = k
        while ans in st:
            ans += k

        return ans
