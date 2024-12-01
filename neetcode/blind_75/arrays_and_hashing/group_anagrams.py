# https://neetcode.io/problems/anagram-groups

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for string in strs:
            frequency = tuple(get_frequency(string))
            if frequency not in res:
                res[frequency] = [string]
            else:
                res[frequency].append(string)
        return res.values()


def get_frequency(string):
    frequency = [0] * 26
    for c in string:
        current_index = ord(c) - ord('a')
        frequency[current_index] += 1
    return frequency