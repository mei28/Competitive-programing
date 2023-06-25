MOD = 998244353
N, M = map(int, input().split())


def power(x, n):
    ans = 1
    while n > 0:
        if n & 1:
            ans = ans * x % MOD
        x = x * x % MOD
        n >>= 1
    return ans


total = M * power(M - 1, N - 1) % MOD
same_first_and_last = M * power(M - 1, N - 2) % MOD if N > 2 else 0

answer = (total - same_first_and_last + MOD) % MOD

print(answer)
