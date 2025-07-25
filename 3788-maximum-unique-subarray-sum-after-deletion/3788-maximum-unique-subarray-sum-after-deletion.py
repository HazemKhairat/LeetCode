class Solution:
    def maxSum(self, nums: List[int]) -> int:
        left, right = 0, 0
        st = set()
        arr = []
        maxi = -inf
        sumPos = 0
        for num in nums:
            if num in st:
                continue
            st.add(num)
            arr.append(num)
            maxi = max(maxi, num)
            if num > 0:
                sumPos += num

        return max(maxi, sumPos) if sumPos > 0 else maxi
        