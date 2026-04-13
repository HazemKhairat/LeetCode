class Solution:
    def repeatLimitedString(self, s: str, k: int) -> str:
        # create array of lenght 26 from a-z char
        chars = [0] * 26
        # build the freq of each char
        for ch in s:
            chars[ord(ch) - 97] += 1
        # print(chars)

        ans = ""
        while True:
            # find the max char in s
            max_char = -1
            for i in range(25, -1, -1):
                if chars[i] > 0:
                    max_char = i
                    break

            # if not found break
            if max_char == -1:
                break

            ans += min(k, chars[max_char]) * (chr(max_char + 97))

            # if max char freq <= k then it's freq = 0
            if chars[max_char] <= k:
                chars[max_char] = 0
            else:
                chars[max_char] -= k
                # if max char freq > k -> find the second max char
                second_max_char = -1
                for i in range(max_char - 1, -1, -1):
                    if chars[i] > 0:
                        second_max_char = i
                        break

                # if not found break
                if second_max_char == -1:
                    break

                # if found take 1 char and substract 1 form it's freq
                ans += chr(second_max_char + 97)
                chars[second_max_char] -= 1

        return ans
