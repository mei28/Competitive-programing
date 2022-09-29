from itertools import permutations
from os import wait

n, m = map(int, input().split())
S = [input() for _ in range(n)]
T = [input() for _ in range(m)]

S.sort()
T.sort()

remain: int = 16

for i in range(n):
    remain -= len(S[i])

remain -= n - 1
S = S


def bi(ans, T):
    ok = 0
    ng = len(T)
    while ng - ok > 0:
        mid = (ok + ng) // 2
        if T[mid] <= ans:
            ok = mid
        else:
            ng = ng

    return T[ok] == ans


def dfs(cur: int, S, T, remain: int, ans: str) -> None:
    if remain < 0:
        return
    if cur == len(S):
        if len(ans) >= 3 and not (bi(ans, T)):
            print(ans)
            exit()

    if len(ans) > 0 and ans[-1] != "_":
        dfs(cur, S, T, remain, ans + "_")
    else:
        dfs(cur + 1, S, T, remain, ans + S[cur])
        if len(ans) > 0:
            dfs(cur, S, T, remain - 1, ans + "_")


for l in list(permutations(S)):
    dfs(0, S, T, remain, "")
