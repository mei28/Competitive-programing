n = int(input())
A = list(map(int, input().split()))
A.sort()
B = set(A)

ok = 0
ng = n + 1

while ng - ok > 1:
    m = (ok + ng) // 2
    c = set(range(1, m + 1)) & B
    c = len(c)

    if c + (n - c) // 2 >= m:
        ok = m
    else:
        ng = m
print(ok)
