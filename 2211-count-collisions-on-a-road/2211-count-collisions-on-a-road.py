class Solution:
    def countCollisions(self, directions: str) -> int:
        arr = list(directions)
        ans = 0
        r = arr[0] == "R"
        s = arr[0] == "S"

        for i in range(1, len(arr)):

            if arr[i] == "L" and arr[i - 1] == "R":
                ans += 2
                arr[i] = arr[i - 1] = "S"
                ans += r - 1 if r else 0
                r = 0
                s = True
            elif arr[i] == "S":
                ans += r if r else 0
                r = 0
                s = True
            elif arr[i] == "L" and s == True:
                ans += 1
                arr[i] = "S"
            elif arr[i] == "R":
                r += 1

        return ans
