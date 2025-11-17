class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        tmp = nums[:]
        tmp.sort()
        ans = []
        for num in nums:
            pos = bisect_left(tmp, num)
            ans.append(pos)
        return ans
