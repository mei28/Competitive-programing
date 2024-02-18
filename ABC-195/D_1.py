n, m, q = map(int, input().split())
WV = []

for _ in range(n):
    w, v = map(int, input().split())
    WV.append((w, v))

WV.sort(key=lambda x: -x[1])
X = list(map(int, input().split()))
Q = []
for i in range(q):
    l, r = map(int, input().split())
    Q.append([l, r])


def check(LR: list) -> int:
    result = 0
    used = [False] * len(LR)

    for w, v in WV:
        for i, cap in enumerate(LR):
            if cap >= w and used[i] == False:
                used[i] = True
                result += v
                break
    return result


for l, r in Q:
    LR = X[: l - 1] + X[r:]
    LR.sort()

    print(check(LR))
