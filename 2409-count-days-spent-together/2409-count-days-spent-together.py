class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        prefix = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

        def to_days(date):
            return prefix[int(date[:2]) - 1] + int(date[3:])

        start = max(to_days(arriveAlice), to_days(arriveBob))
        end = min(to_days(leaveAlice), to_days(leaveBob))

        return max(0, end - start + 1)
