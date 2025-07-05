class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        res = -1
        for key, val in freq.items():
            if key == val:
                res = max(res, key)
        
        return res
