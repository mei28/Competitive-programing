N = int(input())
AT = []
for i in range(N):
    a, t = map(int, input().split())
    AT.append((a, t))


Q = int(input())
X = list(map(int, input().split()))


def calc(c, a, t):
    if t == 1:
        return c + a
    elif t == 2:
        return max(c, a)
    else:
        return min(c, a)


for x in X:
    a, t = AT[0]
    ans = calc(x, a, t)
    for a, t in AT[1:]:
        ans = calc(ans, a, t)

    print(ans)
