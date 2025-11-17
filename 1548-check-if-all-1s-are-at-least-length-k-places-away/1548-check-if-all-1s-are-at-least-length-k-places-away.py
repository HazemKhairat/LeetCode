class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        dis = 0
        first = True
        for i in range(len(nums)):
            if nums[i] == 1 and dis < k and not first:
                return False
            elif nums[i] == 0:
                dis += 1
            else:
                first = False
                dis = 0
        return True
            