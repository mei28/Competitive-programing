from bisect import bisect_left, bisect_right
from os import wait

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.append(-(10**10))
A.append((10**10))
A.sort()

B.sort()

ans = 10**10
for b in B:
    left = bisect_left(A, b)
    right = bisect_right(A, b)

    ans = min(ans, abs(A[left] - b), abs(A[right] - b))
print(ans)
