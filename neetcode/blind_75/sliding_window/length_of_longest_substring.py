# https://neetcode.io/problems/longest-substring-without-duplicates


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            check_set = set()
            count = 0
            for j in range(i, len(s)):
                if s[j] not in check_set:
                    count += 1
                    check_set.add(s[j])
                else:
                    break
            res = max(res, count)
        return res

    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        check_set = set()
        left = 0
        for right in range(len(s)):
            while s[right] in check_set:
                check_set.remove(s[left])
                left += 1
            check_set.add(s[right])
            res = max(res, right - left + 1)
        return res

solution = Solution()
s = "pwwkew"
res = solution.lengthOfLongestSubstring(s)
print(res)