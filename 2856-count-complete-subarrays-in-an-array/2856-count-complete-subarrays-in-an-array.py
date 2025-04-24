class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # ij
        # 0 1 2 3 4
        # 1 3 1 2 2
        # n = 5
        # 5 - 3 = 2, 5 - 3 = 2

        n = len(nums)
        distNums = len(set(nums))

        freq = Counter()
        res = left = 0
        for right in range(n):
            freq[nums[right]] += 1
            while len(freq) == distNums:
                res += n - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    freq.pop(nums[left])
                left += 1

        return res
