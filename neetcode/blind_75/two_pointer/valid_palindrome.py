# https://neetcode.io/problems/is-palindrome


class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_only = []
        for char in s:
            if char.isalpha() or char.isdigit():
                alpha_only.append(char.lower())

        left, right = 0, len(alpha_only) - 1
        while left <= right:
            if alpha_only[left] != alpha_only[right]:
                return False
            left += 1
            right -= 1
        return True