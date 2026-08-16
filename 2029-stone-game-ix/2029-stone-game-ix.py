class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        stones = [(stone % 3) for stone in stones]
        # print(stones)
        cnt0 = stones.count(0)
        cnt1 = stones.count(1)
        cnt2 = stones.count(2)

        if (cnt0 % 2 == 0 and cnt1 > 0 and cnt2 > 0) or (
            cnt0 % 2 == 1 and abs(cnt1 - cnt2) > 2
        ):
            return True
        else:
            return False
