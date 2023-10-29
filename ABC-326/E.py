MOD = 998244353


def expected_salary(N, A):
    # モジュロ計算の逆元を求める関数
    def modinv(x):
        return pow(x, MOD - 2, MOD)

    # 期待値の計算
    E = [0] * (N + 1)
    E[0] = sum(A) * modinv(N) % MOD
    for i in range(1, N + 1):
        E[i] = (E[i - 1] - A[i - 1] * modinv(N) + MOD) % MOD

    ans = E[0]
    for i in range(1, N + 1):
        ans = (ans + E[i] * pow(modinv(N), i + 1, MOD)) % MOD

    return ans


N = int(input())
A = list(map(int, input().split()))

print(expected_salary(N, A))
