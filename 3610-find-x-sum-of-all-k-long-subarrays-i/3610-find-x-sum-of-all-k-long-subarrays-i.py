class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n - k + 1):
            dic = Counter(nums[i : i + k])
            freq = sorted(dic.items(), key=lambda x: (-x[1], -x[0]))
            xsum = sum(key * val for key, val in freq[:x])
            ans.append(xsum)

        return ans
