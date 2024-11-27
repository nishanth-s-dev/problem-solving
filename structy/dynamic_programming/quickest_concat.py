def quickest_concat(s, words):
    res = _quickest_concat(s, words, {})
    return res if res != float('inf') else -1


def _quickest_concat(s, words, memo):
    if not s:
        return 0

    if s not in memo:
        res = float("inf")
        for word in words:
            if s.startswith(word):
                suffix = s[len(word):]
                res = min(res, 1 + _quickest_concat(suffix, words, memo))
        memo[s] = res

    return memo[s]