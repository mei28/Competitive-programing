N = int(input())
A = list(map(int, input().split()))

cnt = 0
for i, a in enumerate(A):
    if A[a - 1] == i + 1:
        cnt += 1


print(cnt // 2)
