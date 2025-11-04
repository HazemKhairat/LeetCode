class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        i, j = 0, k - 1
        ans = []
        while j < len(nums):
            dic = Counter(nums[i:j+1])
            dic = sorted(dic.items(), key=lambda x : (-x[1], -x[0]))
            tmp = x
            res = 0
            for l in range(tmp):
                if l == len(dic): break
                res += dic[l][0] * dic[l][1]
            ans.append(res)
            i += 1
            j += 1

        return ans