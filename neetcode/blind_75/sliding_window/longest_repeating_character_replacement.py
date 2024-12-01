# https://neetcode.io/problems/longest-repeating-substring-with-replacement
from structy.arrays_and_strings.most_frequent_char import most_frequent_char


class Solution:
    def get_most_frequent_char_count(self, string):
        count = 0
        for i in range(len(string)):
            current_count = 0
            for j in range(len(string)):
                if string[i] == string[j]:
                    current_count += 1
            count = max(current_count, count)
        return count

    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                substring = s[i:j]
                most_frequenct_char_count = self.get_most_frequent_char_count(substring)
                steps_needed = len(substring) - most_frequenct_char_count
                if steps_needed <= k:
                    res = max(res, len(substring))
        return res

    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        res = 0

        frequency = [0] * 26
        while left < len(s) and right < len(s):
            frequency[ord(s[right]) - ord("A")] += 1
            right += 1
            most_frequent_char_count = max(frequency)
            steps_needed = (right - left) - most_frequent_char_count
            if steps_needed <= k:
                res = max(res, right - left)
            else:
                frequency[ord(s[left]) - ord("A")] -= 1
                left += 1

        return res



solution = Solution()
res = solution.characterReplacement("ABSGONQDHTGFFDRQENMMRDCCSCHBNASDDGKTDCASIIJCGTCBKPHPOKSGPMCSDLTJCHLSRONMMISHQOJMJGQDFJIGMAEHQDSRHKML", 4)
print(res)