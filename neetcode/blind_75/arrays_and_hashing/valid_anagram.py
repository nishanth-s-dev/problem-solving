# https://neetcode.io/problems/is-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = get_counter(s)
        t_counter = get_counter(t)

        if len(s_counter) != len(t_counter):
            return False

        for key in s_counter:
            if key not in t_counter or s_counter[key] != t_counter[key]:
                return False
        return True


def get_counter(string):
    counter = {}
    for c in string:
        if c not in counter:
            counter[c] = 1
        else:
            counter[c] += 1
    return counter