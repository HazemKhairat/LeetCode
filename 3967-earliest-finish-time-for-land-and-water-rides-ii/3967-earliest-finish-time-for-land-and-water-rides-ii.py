class Solution:
    def earliestFinishTime(self, ls: List[int], ld: List[int], ws: List[int], wd: List[int]) -> int:

        landSum = [ls[i] + ld[i] for i in range(len(ls))]
        waterSum = [ws[i] + wd[i] for i in range(len(ws))]

        minLandSum = min(landSum)
        minWaterSum = min(waterSum)

        option1 = option2 = inf
        for i in range(len(ws)):
            option1 = min(option1, minLandSum + wd[i] if ws[i] <= minLandSum else waterSum[i])

        for i in range(len(ls)):
            option2 = min(option2, minWaterSum + ld[i] if ls[i] <= minWaterSum else landSum[i])

        return min(option1, option2)