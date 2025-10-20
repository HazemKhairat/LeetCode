class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        prev = -inf

        for i in range(len(nums)):
            best = prev + 1  # best result until now
            best = max(best, nums[i] - k)  # min Filter
            best = min(best, nums[i] + k)  # max Filter
            prev = nums[i] = best  # final answer

        return len(set(nums))  # num of distinct items
