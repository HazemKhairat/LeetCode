class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # find maximum or 
        # recurse if index == len(nums) and curr subset or == maxim or return 1
        # else return 0

        maxi = 0
        n = len(nums)
        for num in nums:
            maxi |= num
        
        @cache
        def dfs(index, curr):
            if index == n:
                return curr == maxi

            take = skip = 0
            take += dfs(index + 1, (curr | nums[index]))
            skip += dfs(index + 1, curr)

            return take + skip


        return dfs(0, 0)