mod = 1000000007

fact = [0] * 200009
factinv = [0] * 200009


def modpow(a, b, m):
    p = 1
    q = a

    for i in range(30):
        if (b & (1 << i)) != 0:
            p *= q
            p %= m
        q *= q
        q %= m
    return p


def div(a, b, m):
    return (a * modpow(b, m - 2, m)) % m


def init():
    # 　nCr の逆元を求める
    fact[0] = 1
    for i in range(1, 200000):
        fact[i] = (1 * i * fact[i - 1]) % mod
    for i in range(0, 200000):
        factinv[i] = div(1, fact[i], mod)


def ncr(n, r):
    if n < r or r < 0:
        return 0
    return (fact[n] * factinv[r] % mod) * factinv[n - r] % mod


def query(K):
    ret = 0
    for i in range(1, N // K + 2):
        s1 = N - (K - 1) * (i - 1)
        s2 = i
        ret += ncr(s1, s2)
        ret %= mod


if __name__ == "__main__":
    N = int(input())
    init()

    for i in range(1, N + 1):
        ans = query(i)
        print(ans)
