import sys

sys.setrecursionlimit(1000000)


def dfs(sx: int, sy: int, px: int, py: int) -> int:
    if sx == px and sy == py and visited[px][py]:
        return 0
    visited[px][py] = True
    ret = -100000

    for i in range(4):
        nx = px + dx[i]
        ny = py + dy[i]
        if nx < 0 or ny < 0 or h <= nx or w <= ny or mat[nx][ny] == "#":
            continue
        if (sx != nx or sy != ny) and visited[nx][ny]:
            continue
        v = dfs(sx, sy, nx, ny)
        ret = max(ret, v + 1)

    visited[px][py] = False
    return ret


if __name__ == "__main__":
    h, w = map(int, input().split())
    mat = [input() for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    ans = -1

    for i in range(h):
        for j in range(w):
            ans = max(ans, dfs(i, j, i, j))

    if ans <= 2:
        print(-1)
    else:
        print(ans)
