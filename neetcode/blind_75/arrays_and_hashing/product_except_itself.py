# https://neetcode.io/problems/products-of-array-discluding-self
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            current = 1
            for j in range(len(nums)):
                if i != j:
                    current *= nums[j]
            res.append(current)
        return res