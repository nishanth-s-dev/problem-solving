from typing import List

# https://neetcode.io/problems/two-integer-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in tracker:
                return [tracker[diff], index]
            else:
                tracker[num] = index
        return []