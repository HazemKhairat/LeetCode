class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        ans = ''
        for i in range(len(s)):
            if s[i] == '6':
                ans = s[:i] + '9' + s[i+1:]
                break

        return int(ans) if ans != '' else num