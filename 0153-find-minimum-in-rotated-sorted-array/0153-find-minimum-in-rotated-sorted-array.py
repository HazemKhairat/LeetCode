class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        
        while l < r:
            mid = (l + r) // 2
            # print(nums[mid])
            if nums[mid] >= nums[l]:
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid
            else:
                r = mid
                
        return nums[l]