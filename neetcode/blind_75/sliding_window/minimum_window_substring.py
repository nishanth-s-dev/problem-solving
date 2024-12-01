# https://neetcode.io/problems/minimum-window-with-characters

# TODO : Need to add optimized solution

class Solution:
    def get_frequency(self, string):
        frequency = [0] * 52
        for c in string:
            if 'A' <= c <= 'Z':
                frequency[ord(c) - ord('A')] += 1
            else:
                frequency[ord(c) - ord('a') + 26] += 1

        return frequency

    def minWindow(self, s: str, t: str) -> str:
        res = ""

        t_frequency = self.get_frequency(t)

        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                substring = s[i:j + 1]

                frequency = self.get_frequency(substring)
                flag = True
                for f in range(len(frequency)):
                    t_count = t_frequency[f]
                    current_frequency = frequency[f]
                    if current_frequency < t_count:
                        flag = False
                        break

                if flag and (len(substring) < len(res) or res == ""):
                    res = substring
        return res
