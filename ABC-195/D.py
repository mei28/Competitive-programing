n, m, q = map(int, input().split())

item = []
for i in range(n):
    w, v = map(int, input().split())
    item.append((v, w))


item.sort(reverse=True)


def solve(x):
    x.sort()
    n = len(x)
    used = [False] * n
    ans = 0
    for (v, w) in item:
        for j in range(n):
            if used[j]:
                continue
            if x[j] >= w:
                used[j] = True
                ans += v
                break
    print(ans)


x = list(map(int, input().split()))
for _ in range(q):
    l, r = map(int, input().split())
    solve(x[: l - 1] + x[r:])
