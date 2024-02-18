T = int(input())
L, R = [], []
for i in range(T):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)


def solve(l, r):
    stride = r - l
    cnt = 0
    if l - r == l:
        return 1
    elif l - r == 0:
        return 0
    if l * 2 <= r:
        n = (r - l) - l + 1
        cnt = (n) * (n + 1) // 2
    else:
        cnt = 0
    return cnt


for l, r in zip(L, R):
    print(solve(l, r))
