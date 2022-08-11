n, k = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = []

for i in range(k):
    ans.append(A[i] + A[-i - 1])
for i in range(k, n - k):
    ans.append(A[i])

print(min(ans))
