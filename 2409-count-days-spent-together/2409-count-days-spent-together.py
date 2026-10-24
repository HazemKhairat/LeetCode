class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:

        mDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        months = {}
        for i in range(1, 13):
            months[i] = mDays[i - 1]

        # print(months)

        arriveA_M, arriveA_D = int(arriveAlice[0:2]), int(arriveAlice[3:])
        leaveA_M, leaveA_D = int(leaveAlice[0:2]), int(leaveAlice[3:])
        arriveB_M, arriveB_D = int(arriveBob[0:2]), int(arriveBob[3:])
        leaveB_M, leaveB_D = int(leaveBob[0:2]), int(leaveBob[3:])
        # print(arriveA_M, " ", arriveA_D, " ", leaveA_M, " ", leaveA_D)
        # print(arriveB_M, " ", arriveB_D, " ", leaveB_M, " ", leaveB_D)

        aliceArrive, aliceLeave, bobArrive, bobLeave = 0, 0, 0, 0

        for i in range(1, 13):
            if i < arriveA_M:
                aliceArrive += months[i]
            elif i == arriveA_M:
                aliceArrive += arriveA_D

            if i < leaveA_M:
                aliceLeave += months[i]
            elif i == leaveA_M:
                aliceLeave += leaveA_D

            if i < arriveB_M:
                bobArrive += months[i]
            elif i == arriveB_M:
                bobArrive += arriveB_D

            if i < leaveB_M:
                bobLeave += months[i]
            elif i == leaveB_M:
                bobLeave += leaveB_D

        # print(aliceArrive, " ", aliceLeave)
        # print(bobArrive, " ", bobLeave)

        ans = 0
        for i in range(1, 366):
            if (i >= aliceArrive and i >= bobArrive) and (
                i <= aliceLeave and i <= bobLeave
            ):
                ans += 1

        return ans
