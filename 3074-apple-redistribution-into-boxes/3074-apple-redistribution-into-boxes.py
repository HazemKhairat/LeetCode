class Solution:
    def minimumBoxes(self, apple: List[int], cap: List[int]) -> int:
        ans = 0
        n = len(cap)
        cap.sort()
        total = sum(apple)

        for i in range(n - 1, -1, -1):
            ans += 1
            if total <= cap[i]:
                return ans
            total -= cap[i]
        
        return ans
