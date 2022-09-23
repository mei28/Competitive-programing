import sys

sys.setrecursionlimit(10**7)
n, l, r = map(int, input().split())

ans = set()


def f(a):
    if len(a) == n:
        ans.add(tuple(a))
        return
    else:
        last = a[-1]
        for i in range(max(last, l), r + 1):
            a.append(i)
            f(a)
            a.pop()


for i in range(l, r + 1):
    f([i])
ans = list(ans)
ans.sort()
for a in ans:
    print(*a)
