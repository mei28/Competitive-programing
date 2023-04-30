import sys

sys.setrecursionlimit(10**7)

H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]


def dfs(y, x):
    cnt = 1
    C[y][x] = "."
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            y2, x2 = y + dy, x + dx
            if 0 <= y2 < H and 0 <= x2 < W and C[y2][x2] == "#":
                cnt += dfs(y2, x2)
    return cnt


ans = [0 for _ in range(min(H, W))]
for y in range(H):
    for x in range(W):
        if C[y][x] == "#":
            ans[dfs(y, x) // 4 - 1] += 1
print(" ".join(map(str, ans)))
