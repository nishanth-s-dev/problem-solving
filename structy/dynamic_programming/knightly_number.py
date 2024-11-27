# https://www.structy.net/problems/premium/knightly-number

def knightly_number(n, m, kr, kc, pr, pc):
    return _knightly_number(n, m, kr, kc, pr, pc, {})


def _knightly_number(n, m, kr, kc, pr, pc, memo):
    pos = (kr, kc)
    if not is_inbounds(n, pos):
        return 0

    key = (*pos, m)
    if key in memo:
        return memo[key]

    if m == 0:
        if pos == (pr, pc):
            memo[key] = 1
            return 1
        else:
            memo[key] = 0
            return 0

    neighbors = get_neighbors(pos)
    count = 0
    for neighbor in neighbors:
        neighbor_row, neighbor_col = neighbor
        count += _knightly_number(n, m - 1, neighbor_row, neighbor_col, pr, pc, memo)
    memo[key] = count
    return count


def is_inbounds(n, pos):
    row, col = pos
    return 0 <= row < n and 0 <= col < n


def get_neighbors(pos):
    row, col = pos
    deltas = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    neighbors = []
    for delta in deltas:
        delta_row, delta_col = delta
        neighbors.append((row + delta_row, col + delta_col))

    return neighbors
