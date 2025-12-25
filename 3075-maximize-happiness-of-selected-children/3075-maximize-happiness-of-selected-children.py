class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:

        happiness.sort()
        dec = 0

        ans = 0
        i = len(happiness) - 1
        while k:
            curr = happiness[i] - dec
            ans +=  curr if curr > 0 else 0
            dec += 1
            i -= 1
            k -= 1

        return ans
            