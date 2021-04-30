from collections import Counter

N = int(input())
tiles = [[0 for i in range(1010)] for _ in range(1010)]

for i in range(N):
    lx, ly, rx, ry = map(int, input().split())
    # 左下
    tiles[ly][lx] += 1
    # 左上
    tiles[ry][lx] -= 1
    # 右下
    tiles[ly][rx] -= 1
    # 右上
    tiles[ry][rx] += 1

# 横方向の累積和

for y in range(1001):
    for x in range(1001):
        tiles[y][x + 1] += tiles[y][x]

# 縦方向の累積和
for x in range(1001):
    for y in range(1001):
        tiles[y + 1][x] += tiles[y][x]

ans = []
for i in tiles:
    ans += i

cnter = Counter(ans)

for i in range(1, N + 1):
    if i in cnter.keys():
        print(cnter[i])
    else:
        print(0)
