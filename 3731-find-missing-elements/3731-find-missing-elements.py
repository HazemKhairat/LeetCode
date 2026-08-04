class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini = min(nums)
        maxi = max(nums)
        tmp = set(nums)
        res = []
        for i in range(mini + 1, maxi):
            if i not in tmp:
                res.append(i)

        return res