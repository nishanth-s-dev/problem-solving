from typing import List

# https://neetcode.io/problems/max-water-container


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = float("-inf")
        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)):
                res = max(min(heights[i], heights[j]) * (j - i), res)
        return res

    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        res = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            res = max(area, res)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return res