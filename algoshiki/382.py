n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()

for b in B:
    ok = n
    ng = -1

    while ok - ng > 1:
        mid = (ok + ng) // 2
        if b < A[mid]:
            ok = mid
        else:
            ng = mid

    print(ok)
