n, x = map(int, input().split())
A = list(map(int, input().split()))

_sum = 0
for i, a in enumerate(A):
    if (i + 1) % 2 == 0:
        _sum += a - 1
    else:
        _sum += a

if _sum <= x:
    print("Yes")
else:
    print("No")
