import math
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())


def can_move(a, b):
    ans = set()
    t = 1000000
    for i in range(t):
        ans.add((a+i, b+i))
        ans.add((a+i, b-i))
        ans.add((a-i, b+i))
        ans.add((a-i, b-i))
    ans.add((a+0, b-3))

    ans.add((a-2, b-2))
    ans.add((a-1, b-2))
    ans.add((a, b-2))
    ans.add((a+2, b-2))
    ans.add((a+1, b-2))

    ans.add((a-2, b-1))
    ans.add((a-1, b-1))
    ans.add((a, b-1))
    ans.add((a+2, b-1))
    ans.add((a+1, b-1))

    ans.add((a-3, b))
    ans.add((a-2, b))
    ans.add((a-1, b))
    ans.add((a, b))
    ans.add((a+2, b))
    ans.add((a+1, b))
    ans.add((a+3, b))

    ans.add((a-2, b+1))
    ans.add((a-1, b+1))
    ans.add((a, b+1))
    ans.add((a+2, b+1))
    ans.add((a+1, b+1))

    ans.add((a-2, b+2))
    ans.add((a-1, b+2))
    ans.add((a, b+2))
    ans.add((a+2, b+2))
    ans.add((a+1, b+2))

    ans.add((a, b+3))

    ans = list(ans)
    return ans


def dist(S, G):
    return math.sqrt((S[0]-G[0])**2 + (S[1]-G[1])**2)


def min_dist(S: set, cm: list):
    min_dist = -1
    min_move = set()
    for c in cm:
        _dist = dist(S, c)
        if _dist < min_dist or min_dist == -1:
            min_move = c
            min_dist = _dist

    return min_move


cnt = 0
if r1 == r2 and c1 == c2:
    print(0)
    exit(0)
for i in range(10000):
    cm = can_move(r1, c1)
    cnt += 1
    if (r2, c2) in cm:
        print(cnt)
        exit()
    a = min_dist((r2, c2), cm)
    print(a)
    r1, c1 = a[0], a[1]
