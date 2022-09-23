import sys

sys.setrecursionlimit(10**7)
l, r = map(int, input().split())


def func(n, l, r):
    if l > r:
        return []
    if n == 0:
        return [""]
    ans = []
    for x in func(n - 1, l, r):
        ans.append(str(l) + x)
    for x in func(n, l + 1, r):
        ans.append(x)
    return ans


ans = 0
for x in func(10, 0, 9):
    if l <= int(x) <= r:
        ans += int(x)
print(ans)
