class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2

        cnt = Counter(nums)

        for key, val in cnt.items():
            if val == n:
                return key
        return 0