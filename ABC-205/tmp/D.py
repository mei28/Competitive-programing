import bisect

n, q = map(int, input().split())
A = list(map(int, input().split()))
S = [A[i] - (i + 1) for i in range(n)]


for _ in range(q):
    k = int(input())
    i = bisect.bisect_left(S, k)
    if i == 0:
        print(k)
    else:
        print(A[i - 1] + (k - S[i - 1]))
