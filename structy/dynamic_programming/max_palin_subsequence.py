# https://www.structy.net/problems/max-palin-subsequence


def max_palin_subsequence(string):
  return _max_palin_subsequence(string, 0, len(string) - 1, {})

def _max_palin_subsequence(string, start, end, memo):
  if start == end:
    return 1
  if start > end:
    return 0

  pos = (start, end)
  if pos not in memo:
    if string[start] == string[end]:
      memo[pos] =  2 + _max_palin_subsequence(string, start + 1, end - 1, memo)
    else:
      memo[pos] = max(_max_palin_subsequence(string, start + 1, end, memo), _max_palin_subsequence(string, start, end - 1, memo))
  return memo[pos]