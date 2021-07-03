n, k = map(int, input().split())
A = list(map(int, input().split()))

right = 0
_sum = 0
ans = 0

for left in range(n):
    while right < n and _sum < k:
        _sum += A[right]
        right += 1

    if _sum >= k:
        ans += n - right + 1

    _sum -= A[left]

print(ans)
