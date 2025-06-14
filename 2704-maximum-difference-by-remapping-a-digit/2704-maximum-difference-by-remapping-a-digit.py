class Solution:
    def minMaxDifference(self, num: int) -> int:
        maxStr, minStr = list(str(num)), list(str(num))
        firstDigit = ""

        for i in range(len(maxStr)):
            if maxStr[i] != "9":
                firstDigit = maxStr[i]
                break

        for i in range(len(maxStr)):
            if maxStr[i] == firstDigit:
                maxStr[i] = "9"

        firstDigit = minStr[0]
        for i in range(len(minStr)):
            if minStr[i] == firstDigit:
                minStr[i] = "0"

        num1, num2 = int("".join(maxStr)), int("".join(minStr))

        return num1 - num2
