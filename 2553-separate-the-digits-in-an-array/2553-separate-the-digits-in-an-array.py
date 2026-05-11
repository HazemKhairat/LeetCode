class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        def spearte(num):
            arr = []
            while num:
                arr.append(num % 10)
                num //= 10
            return arr[::-1]

        ans = []
        for num in nums:
            ans = ans + spearte(num)
        
        return ans

