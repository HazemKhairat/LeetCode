class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:

        n = len(nums1)
        even = [num for num in nums1 if num % 2 == 0]
        odd = [num for num in nums1 if num % 2 == 1]
        

        def find(i, parity):
            pos = -1
            if parity == 1:
                if nums1[i] % 2 == 0:
                    pos = bisect.bisect_right(odd, nums1[i])
                else:
                    pos = bisect.bisect_right(even, nums1[i])
            else:
                if nums1[i] % 2 == 0:
                    pos = bisect.bisect_right(odd, nums1[i])
                else:
                    pos = bisect.bisect_right(even, nums1[i])
                    
            return pos != -1
                    

        def solve(parity):
            for i in range(n):
                if (nums1[i] % 2 != parity) and (not find(i, parity)):
                    return False

            return True

        return solve(0) or solve(1)
