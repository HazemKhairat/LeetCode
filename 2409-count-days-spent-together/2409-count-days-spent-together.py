class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def month_to_day(date):
            m, d = int(date[0:2]), int(date[3:])
            return sum(months[: m - 1]) + d

        alice_start, alice_end, bob_start, bob_end = (
            month_to_day(arriveAlice),
            month_to_day(leaveAlice),
            month_to_day(arriveBob),
            month_to_day(leaveBob),
        )

        start = max(alice_start, bob_start)
        end = min(alice_end, bob_end)

        return max(0, end - start + 1)
