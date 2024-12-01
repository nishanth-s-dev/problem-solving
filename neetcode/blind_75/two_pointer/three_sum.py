from typing import List

# https://neetcode.io/problems/three-integer-sum


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) < 3:
            return res

        nums.sort()
        i = 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1

            while j < k:
                current_vals = [nums[i], nums[j], nums[k]]
                current_sum = sum(current_vals)
                if current_sum < 0:
                    j += 1
                elif current_sum > 0:
                    k -= 1
                else:
                    res.append(current_vals)
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
            while i < len(nums) - 2 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res