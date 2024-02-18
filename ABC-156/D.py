n, a, b = map(int, input().split())
MOD = 1000000007

# ans = 2^n - nCa - nCb - 1


def cmb(n: int, k: int, fac: list, ifac: list, mod: int = 1000000070):
    k = min(k, n - k)
    return fac[n] * ifac[n - k] % mod * ifac[k] % mod


def make_tables(n: int, mod: int) -> tuple:
    """
    階乗のテーブル，逆元の階乗のテーブルを作成する
    """
    # 階乗テーブル
    fac = [1, 1]
    # 逆元のテーブル
    inverse = [0, 1]
    # 逆元階乗のテーブル
    ifac = [1, 1]

    for i in range(2, n + 1):
        fac.append((fac[-1] * i) % mod)
        inverse.append(-inverse[mod % i] * (mod // i) % mod)
        ifac.append((ifac[-1] * inverse[-1]) % mod)

    return fac, ifac


fac, ifac = make_tables(n, MOD)

ans = 2**n - cmb(n, a, fac, ifac, MOD) - cmb(n, b, fac, ifac, MOD) - 1
print(ans % MOD)
