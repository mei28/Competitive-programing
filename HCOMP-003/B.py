n = int(input())
A = list(map(int, input().split()))
A.sort()

import math

ans = A[-1]
for i in range(n - 1):
    ans = math.gcd(ans, A[i])
print(ans)
