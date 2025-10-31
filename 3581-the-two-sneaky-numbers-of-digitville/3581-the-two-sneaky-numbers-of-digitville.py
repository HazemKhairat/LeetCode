class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        ans = []
        for key, val in cnt.items():
            if val > 1:
                ans.append(key)
            
        return ans