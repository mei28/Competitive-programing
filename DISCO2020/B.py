N = int(input())
A = list(map(int, input().split()))

c = 0
d = sum(A)
res = 999999999999999999999999

for i in range(N):
    c += A[i]
    d -= A[i]
    res = min(res, abs(c-d))

print(res)
