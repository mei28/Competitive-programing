n, k = map(int, input().split())
A = list(map(int, input().split()))
MOD = 1000000007

ans = 0
for i in range(n):
    migi = 0
    zentai = 0
    for j in range(i, n):
        if A[i] > A[j]:
            migi += 1
    for j in range(n):
        if A[i] > A[j]:
            zentai += 1

    ans += migi * k % MOD
    ans %= MOD
    ans += (k - 1) * k // 2 % MOD * zentai % MOD
    ans %= MOD

print(ans)
