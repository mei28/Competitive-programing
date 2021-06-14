n, q = map(int, input().split())
a = list(map(int, input().split()))


def cnt(m):
    bottom, top = 0, n
    while top - bottom > 1:
        mid = (top + bottom) // 2
        if a[mid] <= m:
            bottom = mid
        else:
            top = mid
    if m < a[0]:
        top = 0
    return m - top


def solve(k):
    bottom, top = 0, 10 ** 19
    while top - bottom > 1:
        mid = (top + bottom) // 2
        if cnt(mid) < k:
            bottom = mid
        else:
            top = mid
    return top


for _ in range(q):
    k = int(input())
    print(solve(k))
