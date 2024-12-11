class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")" :"(", "}" : "{", "]" : '['}
        stack = []
        for bracket in s:
            if bracket not in pairs:
                stack.append(bracket)
            else:
                if not stack or stack.pop() != pairs[bracket]:
                    return False

        return not stack