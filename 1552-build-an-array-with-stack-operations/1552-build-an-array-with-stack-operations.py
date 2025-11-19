class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target = [0] + target
        ans = []
        i = 1
        while i < len(target):
            diff = target[i] - target[i - 1] - 1
            while diff > 0:
                ans.append("Push")
                ans.append("Pop")
                diff -= 1
            ans.append("Push")
            i += 1

        return ans
