class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1] 
        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        for index, num in enumerate(nums):
            if target - num in diff_map:
                return [diff_map[target - num], index]
            diff_map[num] = index
        return [-1]