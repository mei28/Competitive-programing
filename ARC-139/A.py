n = int(input())
T = list(map(int, input().split()))

ans = 0
for i, t in enumerate(T):
    pt = 1 << t
    ans = (ans // pt + 1) * pt
    if ans % (pt * 2) == 0:
        ans += pt

print(ans)
