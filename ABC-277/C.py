import sys

sys.setrecursionlimit(10**7)
n = int(input())
A = []
B = []
AB = {}
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    if a > b:
        a, b = b, a
    if a not in AB.keys():
        AB[a] = AB.setdefault(a, [])
    AB[a].append(b)


ans = 1


def dfs(a):
    global ans
    if a not in AB.keys():
        ans = max(a, ans)
        # print(ans)
        return

    for v in AB[a]:
        dfs(v)


dfs(1)
print(ans)
