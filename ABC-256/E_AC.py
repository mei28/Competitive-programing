import sys

sys.setrecursionlimit(10**7)
n = int(input())
X = [-1] + list(map(int, input().split()))
C = [-1] + list(map(int, input().split()))

checked = [False] * (n + 1)
come = [False] * (n + 1)


ans = 0


def check(v):
    global ans
    if checked[v]:
        return
    if come[v]:
        tmp = C[v]
        now = X[v]
        while now != v:
            tmp = min(tmp, C[now])
            now = X[now]
        ans += tmp
        return
    come[v] = True
    check(X[v])
    checked[v] = True


for i in range(1, n + 1):
    check(i)

print(ans)
