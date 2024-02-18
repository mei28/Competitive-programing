A = list(map(int, input().split()))

A.sort()

diff = A[2] - A[0] + A[2] - A[1]
ans = 0
ans = diff // 2
if diff % 2 == 1:
    ans += 2

print(ans)
