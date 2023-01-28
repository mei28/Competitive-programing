import sys

sys.setrecursionlimit(10**7)
n = int(input())
G = [[] for _ in range(n)]

for i in range(n):
    m = int(input())
    for _ in range(m):
        s, t = map(int, input().split())
        G[i].append((s, s + t))


ans = 0


def check(A):
    global ans
    A = list(sorted(A, key=lambda x: x[1]))

    res = 0
    last_time = 0
    for s, t in A:
        if last_time <= s:
            last_time = t
            res += 1
    ans = max(ans, res)


def dfs(A):
    if len(A) == n:
        check(A)
        return

    m = len(A)
    for i in range(len(G[m])):
        A.append(G[m][i])
        dfs(A)
        A.pop()


dfs([])
print(ans)
