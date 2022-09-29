n, k = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

count = []

for a in A:
    b = k - a
    ng = -1
    ok = n
    while ok - ng > 1:
        mid = (ok + ng) // 2

        if b <= A[mid]:
            ok = mid
        else:
            ng = mid
    count.append(n - ok)
print(sum(count))
