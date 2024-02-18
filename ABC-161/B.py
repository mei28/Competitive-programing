N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
_sum = sum(A)
for i in A:
    if i >= _sum / (4 * M):
        cnt += 1

if cnt >= M:
    print("Yes")
else:
    print("No")
