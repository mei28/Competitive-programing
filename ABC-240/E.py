import sys

sys.setrecursionlimit(10**7)

N = int(input())

edge = [[] for _ in range(N)]

leaf = 1

ans = [0] * N

for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)


def dfs(x, last=-1):
    global leaf
    child_cnt = 0
    ans[x] = [leaf, leaf]
    for to in edge[x]:
        if to == last:
            continue
        child_cnt += 1
        dfs(to, x)
        ans[x][1] = max(ans[x][1], ans[to][1])

    if ans[x][1] == leaf:
        leaf += 1


dfs(0)

for i in range(N):
    print(*ans[i])
