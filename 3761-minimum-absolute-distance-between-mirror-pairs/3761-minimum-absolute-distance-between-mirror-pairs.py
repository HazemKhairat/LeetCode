from collections import defaultdict

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        dic = defaultdict(deque)
        n = len(nums)
        for i in range(n):
            dic[nums[i]].append(i)

        def helper(num):
            num = str(num)
            num = num[::-1]
            num = int(num)
            return num
        
        ans = inf
        for i in range(n):
            dic[nums[i]].popleft()
            num = helper(nums[i])
            if num in dic and dic[num]:
                ans = min(ans, dic[num][0] - i)
                
        return ans if ans != inf else -1