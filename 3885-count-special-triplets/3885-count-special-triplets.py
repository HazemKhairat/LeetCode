MOD = 10**9 + 7

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        leftSet, rightSet = Counter(nums[:1]), Counter(nums[1:])
        
        res = 0
        for i in range(1, len(nums)):
            curr = nums[i] * 2 
            if nums[i] in rightSet:
                rightSet[nums[i]] -= 1
                if rightSet[nums[i]] == 0:
                    rightSet.pop(nums[i])
                    
            if curr in leftSet and curr in rightSet:
                res += (leftSet[curr] * rightSet[curr]) % MOD
            leftSet[nums[i]] += 1

        return res % MOD
            
        