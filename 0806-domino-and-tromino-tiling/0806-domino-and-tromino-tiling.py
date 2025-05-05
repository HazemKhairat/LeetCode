class Solution:
    @cache
    def numTilings(self, n, prev_gap=False) -> int:
        if n < 0:
            return 0
        if n == 0:
            return not prev_gap

        if prev_gap:
            return (
                self.numTilings(n - 1) + self.numTilings(n - 1, True)
            ) % 1_000_000_007

        return (
            self.numTilings(n - 1)
            + self.numTilings(n - 2)
            + 2 * self.numTilings(n - 2, True)
        ) % 1_000_000_007
