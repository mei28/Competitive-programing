n = int(input())
A = list(map(int, input().split()))
# 交互に最大化，最小化を行いたい

for i in range(n - 1, 0, -1):
    for j in range(i):
        if i % 2 == 1:
            # minimize
            A[j] = max(A[j], A[j + 1])
            pass
        else:
            # maximize
            A[j] = min(A[j], A[j + 1])
    A.pop()
print(A[0])
