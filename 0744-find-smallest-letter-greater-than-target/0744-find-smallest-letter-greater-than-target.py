class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Binary Search : upper_bound algorithm

        n = len(letters)
        # i, j = 0, n - 1

        # while i <= j:
        #     mid = (i + j) // 2
        #     if letters[mid] > target:
        #         j = mid - 1
        #     elif letters[mid] <= target:
        #         i = mid + 1

        # return letters[i] if i < n else letters[0]

        ans = letters[0]
        for i in range(n - 1, -1, -1):
            if letters[i] > target:
                ans = letters[i]
        return ans
