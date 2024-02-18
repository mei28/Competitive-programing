#  5
# 4136 -> サイコロのインデックス
#  2
#     UP
# left413Right
#     Down


class Dice:
    def __init__(self, surface: list):
        self.surface = surface

    def up(self):
        self.surface[0] = self.surface[1]
        # 回転
        self.surface[1] = self.surface[2]
        self.surface[2] = self.surface[6]
        self.surface[6] = self.surface[5]
        self.surface[5] = self.surface[0]

        return self.surface

    def down(self):
        self.surface[0] = self.surface[1]
        # 回転
        self.surface[1] = self.surface[5]
        self.surface[5] = self.surface[6]
        self.surface[6] = self.surface[2]
        self.surface[2] = self.surface[0]

        return self.surface

    def left(self):
        self.surface[0] = self.surface[1]
        # 回転
        self.surface[1] = self.surface[3]
        self.surface[3] = self.surface[6]
        self.surface[6] = self.surface[4]
        self.surface[4] = self.surface[0]

        return self.surface

    def right(self):
        self.surface[0] = self.surface[1]
        # 回転
        self.surface[1] = self.surface[4]
        self.surface[4] = self.surface[6]
        self.surface[6] = self.surface[3]
        self.surface[3] = self.surface[0]

        return self.surface

    def getNum(self, idx: int) -> int:
        return self.surface[idx]


N, M, Q = map(int, input().split())
# 訪ねたかどうか
visited = [[False for _ in range(M)] for _ in range(N)]

# dct key: (s,t), val: x
dct = {}
for y in range(N):
    for x in range(M):
        dct[(y, x)] = 0
for _ in range(Q):
    s, t, x = map(int, input().split())
    dct[(s, t)] = x

dice = Dice([0, 1, 2, 4, 3, 5, 6])


def dfs(x, y, visited, dct, dice_list):
    # 番外
    if x < 0 or y < 0 or M <= x or N <= y:
        return
    # 訪問済み
    if visited[y][x]:
        return
    # 制約
    if dct[(y, x)] == dice_list[1]:
        visited[y][x] = False
        return

    visited[y][x] = True
    dice = Dice(dice_list)
    dfs(x + 1, y, visited, dct, dice.right())
    dice = Dice(dice_list)
    dfs(x - 1, y, visited, dct, dice.left())
    dice = Dice(dice_list)
    dfs(x, y + 1, visited, dct, dice.down())
    dice = Dice(dice_list)
    dfs(x, y - 1, visited, dct, dice.up())


dfs(0, 0, visited, dct, dice.surface)

if visited[N - 1][M - 1]:
    print("YES")
    if N == 1 or M == 1:
        print(N * M - 1)
    else:
        print(N * M // 2)
else:
    print("NO")
