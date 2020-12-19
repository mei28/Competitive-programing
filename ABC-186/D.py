N = int(input())
A = list(map(int, input().split()))


A.sort()

upper = A[:]

for i in range(N - 2, -1, -1):
    upper[i] += upper[i+1]


ans = 0

for i in range(N - 1):
    ans += upper[i+1] - A[i]*(N-i-1)

print(ans)
