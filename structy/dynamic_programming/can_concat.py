# https://www.structy.net/problems/can-concat

def can_concat(s, words):
    return _can_concat(s, words, 0, {})


def _can_concat(s, words, i, memo):
    if i == len(s):
        return True
    if i not in memo:
        for word in words:
            if s[i:].startswith(word):
                if _can_concat(s, words, i + len(word), memo):
                    memo[i] = True
                    break
        else:
            memo[i] = False
    return memo[i]


res = can_concat("oneisnone", ["one", "none", "is"])  # -> True
print(res)