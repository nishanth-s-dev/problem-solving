# https://neetcode.io/problems/validate-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }
        stack = []
        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                if not stack:
                    return False
                current = stack.pop()
                if brackets[current] != char:
                    return False

        return not stack