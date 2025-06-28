class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        tmp = list(nums)
        tmp.sort()
        n = len(tmp) - 1
        dic = Counter()
        while n >= 0 and k:
            dic[tmp[n]] += 1
            n -= 1
            k -= 1

        res = []
        n = len(nums)
        for i in range(n):
            print(nums[i])
            if dic[nums[i]] > 0:
                res.append(nums[i])
                dic[nums[i]] -= 1

        return res
