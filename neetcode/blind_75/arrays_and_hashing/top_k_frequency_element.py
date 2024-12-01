# https://neetcode.io/problems/top-k-elements-in-list

from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sorted_counter = sorted(counter.keys(), key = lambda x : counter[x])
        return sorted_counter[-k:]