class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:

        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        arriveA_M, arriveA_D = int(arriveAlice[0:2]), int(arriveAlice[3:])
        leaveA_M, leaveA_D = int(leaveAlice[0:2]), int(leaveAlice[3:])
        arriveB_M, arriveB_D = int(arriveBob[0:2]), int(arriveBob[3:])
        leaveB_M, leaveB_D = int(leaveBob[0:2]), int(leaveBob[3:])
        # print(arriveA_M, " ", arriveA_D, " ", leaveA_M, " ", leaveA_D)
        # print(arriveB_M, " ", arriveB_D, " ", leaveB_M, " ", leaveB_D)

        def helper(MM, DD):
            return sum(months[: MM - 1]) + DD

        aliceArrive, aliceLeave, bobArrive, bobLeave = (
            helper(arriveA_M, arriveA_D),
            helper(leaveA_M, leaveA_D),
            helper(arriveB_M, arriveB_D),
            helper(leaveB_M, leaveB_D),
        )

        start = max(aliceArrive, bobArrive)
        end = min(aliceLeave, bobLeave)

        return max(0, end - start + 1)
