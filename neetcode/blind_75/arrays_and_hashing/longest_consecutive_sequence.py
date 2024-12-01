# https://neetcode.io/problems/longest-consecutive-sequence

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))

        current = 1
        result = 1

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if diff == 1:
                current += 1
            else:
                result = max(current, result)
                current = 1

        return max(current, result)