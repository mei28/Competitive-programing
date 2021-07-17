from typing import List

n, m = map(int, input().split())
P, Y = [], []
for _ in range(m):
    p, y = map(int, input().split())
    p -= 1
    P.append(p)
    Y.append(y)

vals = [[] for _ in range(n)]

for i in range(m):
    vals[P[i]].append(Y[i])

for v in range(n):
    # 重複削除
    tmp = set(vals[v])
    vals[v] = list(tmp)
    vals[v].sort()


def lower_bound(l: List[int], target: int) -> int:
    ok = 0
    ng = len(l)
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if l[mid] <= target:
            ok = mid
        else:
            ng = mid
    return ok


for i in range(m):
    v = P[i]
    print(f"{v+1:06}", end="")
    _id = lower_bound(vals[v], Y[i])
    print(f"{_id+1:06}")
