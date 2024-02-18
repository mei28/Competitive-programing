n, k = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

j = 0
for i in range(n):
    j = max(j, i + 1)
    while j < n and A[j] - A[i] <= k:
        j += 1
    ans += j - i - 1
print(ans)
