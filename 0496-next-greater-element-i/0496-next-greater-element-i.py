class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n, m = len(nums1), len(nums2)
        res = []
        for i in range(n):
            ok = True
            found = False
            for j in range(m):
                
                if nums2[j] > nums1[i] and found:
                    res.append(nums2[j])
                    ok = False
                    break
                elif nums2[j] == nums1[i]:
                    found = True
            if ok:
                res.append(-1)
        
        return res