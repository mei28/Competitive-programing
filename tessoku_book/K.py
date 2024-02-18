n, x = map(int, input().split())
A = list(map(int, input().split()))

ok = 0
ng = n

while ng - ok > 1:
    mid = (ok + ng) // 2
    if A[mid] <= x:
        ok = mid
    else:
        ng = mid
print(ok + 1)
