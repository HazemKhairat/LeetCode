class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        n, m = len(spells), len(potions)

        def search(num):
            l, r = 0, len(potions) - 1

            while l <= r:
                m = (l + r) // 2
                if num * potions[m] >= success:
                    r = m - 1
                else:
                    l = m + 1

            return l

        ans = []
        for num in spells:
            idx = search(num)
            ans.append(m - idx)

        return ans
