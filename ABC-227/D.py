n, k = map(int, input().split())
A = list(map(int, input().split()))


ok = 0
ng = 1 << 30

while ng - ok > 1:
    md = (ok + ng) // 2
    sum_ = 0

    for x in A:
        sum_ += min(x, md)

    if sum_ >= k * md:
        ok = md
    else:
        ng = md

print(ok)
