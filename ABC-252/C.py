n = int(input())
S = [input() for _ in range(n)]

m = len(S[0])
cost = [0] * m


def solve(i: int):
    cnt = {}
    for s in S:
        idx = s.index(str(i))
        cnt[idx] = cnt.setdefault(idx, 0) + 1

    ret = 0
    for k, v in cnt.items():
        ret = max(ret, (v - 1) * m + k)
    return ret


for i in range(m):
    cost[i] = solve(i)

print(min(cost))
