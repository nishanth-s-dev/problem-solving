# https://www.structy.net/problems/premium/overlap-subsequence

def overlap_subsequence(string_1, string_2):
  return _overlap_subsequence(string_1, string_2, 0, 0, {})

def _overlap_subsequence(string_1, string_2, start_1, start_2, memo):
  if start_1 >= len(string_1) or start_2 >= len(string_2):
    return 0
  pos = (start_1, start_2)
  if pos not in memo:
    if string_1[start_1] == string_2[start_2]:
      memo[pos] = 1 + _overlap_subsequence(string_1, string_2, start_1 + 1, start_2 + 1, memo)
    else:
      memo[pos] = max(_overlap_subsequence(string_1, string_2, start_1 + 1, start_2, memo), _overlap_subsequence(string_1, string_2, start_1, start_2 + 1, memo))

  return memo[pos]