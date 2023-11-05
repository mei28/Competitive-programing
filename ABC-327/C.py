A = [list(map(int, input().split())) for _ in range(9)]


def is_valid_sudoku(grid):
    for i in range(9):
        row = set()
        col = set()
        block = set()

        for j in range(9):
            if grid[i][j] in row or grid[i][j] < 1 or grid[i][j] > 9:
                return "No"
            row.add(grid[i][j])

            if grid[j][i] in col:
                return "No"
            col.add(grid[j][i])

            block_row = 3 * (i // 3)
            block_col = 3 * (i % 3)
            if grid[block_row + j // 3][block_col + j % 3] in block:
                return "No"
            block.add(grid[block_row + j // 3][block_col + j % 3])

    return "Yes"


print(is_valid_sudoku(A))
