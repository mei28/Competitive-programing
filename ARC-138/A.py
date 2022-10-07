from bisect import bisect_right

N, K = map(int, input().split())
A = list(map(int, input().split()))

S1 = A[:K]
S2 = [A[K]]
for x in A[K + 1 :]:
    S2.append(max(S2[-1], x))

ans = 1 << 60
for i, x in enumerate(S1):
    j = bisect_right(S2, x)
    if j < len(S2):
        ans = min(ans, K + j - i)

print(ans if ans < 1 << 60 else -1)
