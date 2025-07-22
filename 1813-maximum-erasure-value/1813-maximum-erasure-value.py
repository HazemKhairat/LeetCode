class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        freq = Counter()
        n = len(nums)
        i, j= 0, 0
        Sum = 0
        maxi = 0
        while j < n:
            Sum += nums[j]
            freq[nums[j]] += 1
            while freq[nums[j]] > 1:
                Sum -= nums[i]
                freq[nums[i]] -= 1
                if freq[nums[i]] == 0:
                    freq.pop(nums[i])
                i += 1
            j += 1
            maxi = max(maxi, Sum)
        return maxi