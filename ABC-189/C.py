N = int(input())
A = list(map(int, input().split()))

table = [[0 for _ in range(N)] for _ in range(N)]

for l in range(N):
    for r in range(l, N):
        table[l][r] = min(A[l:r+1])*(r-l+1)
max_ = 0
for l in table:
    max_ = max(max(l), max_)

print(max_)
