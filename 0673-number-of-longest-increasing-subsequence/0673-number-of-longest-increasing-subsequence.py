class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        l = [1] * n
        cnt = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if l[j] + 1 > l[i]:
                        l[i] = l[j] + 1
                        cnt[i] = 0
                    if l[j] + 1 == l[i]:
                        cnt[i] += cnt[j]


        lis = max(l)
        res = 0
        for i in range(n):
            if l[i] == lis:
                res += cnt[i]
                
        return res