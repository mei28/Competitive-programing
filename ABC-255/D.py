from bisect import bisect_left

n, q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

S = [0] * (n + 1)
for i in range(n):
    S[i + 1] = S[i] + A[i]
for _ in range(q):
    x = int(input())
    ok = bisect_left(A, x)
    ans = x * ok
    ans -= S[ok]
    ans += S[n] - S[ok]
    ans -= x * (n - ok)
    print(ans)
