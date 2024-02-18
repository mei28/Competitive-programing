N = int(input())
A = list(map(int, input().split()))

top1 = max(A[: 2 ** (N - 1)])
top2 = max(A[2 ** (N - 1) :])

if top1 > top2:
    print(A.index(top2) + 1)
else:
    print(A.index(top1) + 1)
