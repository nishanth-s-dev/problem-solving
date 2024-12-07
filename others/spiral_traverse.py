matrix = [
    [1, 2, 3],
    [12, 13, 4],
    [11, 14, 5],
    [10, 15, 6],
    [9, 8, 7]
]

def check_bounds(start_row, end_row, start_col, end_col):
    return start_row <= end_row and start_col <= end_col


def spiral_matrix(matrix):
    start_row, end_row = 0, len(matrix) - 1
    start_col, end_col = 0, len(matrix[0]) - 1
    res = []


    while check_bounds(start_row, end_row, start_col, end_col):
        # left   -> right  || start_col -> end_col 
        for i in range(start_col, end_col + 1):
            res.append(matrix[start_row][i])
        start_row += 1

        # top    -> bottom || start_row -> end_row
        for i in range(start_row, end_row + 1):
            res.append(matrix[i][end_col])
        end_col -= 1

        # right  -> left   || end_col   -> start_col
        if check_bounds(start_row, end_row, start_col, end_col):
            for i in range(end_col, start_col - 1, -1):
                res.append(matrix[end_row][i])
            end_row -= 1

        # bottom -> top    || end_row   -> start_row
        if check_bounds(start_row, end_row, start_col, end_col):
            for i in range(end_row, start_row - 1, -1):
                res.append(matrix[i][start_col])
            start_col += 1

    return res

print(spiral_matrix(matrix))