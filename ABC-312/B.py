N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]

tak_code = [
    ["#" * 3 + "." * 3 + "#" * 3 for _ in range(3)],
    ["." * 9 for _ in range(3)],
    ["#" * 3 + "." * 3 + "#" * 3 for _ in range(3)],
]


def show(grid):
    print("=" * 20)
    for g in grid:
        print(g)


def check(grid):
    flg = grid[0][0] == grid[0][1] == grid[0][2] == "#" and grid[0][3] == "."
    flg = grid[1][0] == grid[1][1] == grid[1][2] == "#" and grid[1][3] == "." and flg
    flg = grid[2][0] == grid[2][1] == grid[2][2] == "#" and grid[2][3] == "." and flg
    flg = grid[3][0] == grid[3][1] == grid[3][2] == grid[3][3] == "." and flg

    flg = grid[8][5] == "." and grid[8][6] == grid[8][7] == grid[8][8] == "#" and flg
    flg = grid[7][5] == "." and grid[7][6] == grid[7][7] == grid[7][8] == "#" and flg
    flg = grid[6][5] == "." and grid[6][6] == grid[6][7] == grid[6][8] == "#" and flg
    flg = grid[5][5] == grid[5][6] == grid[5][7] == grid[5][8] == "." and flg
    return flg


for i in range(N - 8):
    for j in range(M - 8):
        area = [row[j : j + 9] for row in grid[i : i + 9]]
        if check(area):
            print(i + 1, j + 1)
