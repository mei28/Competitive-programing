x, y = map(int, input().split())
MOD = 1000000007


def nCk(n: int, k: int, fac: list, ifac: list, mod: int = MOD):
    """nCkの計算"""
    k = min(k, n - k)
    return fac[n] * ifac[k] % mod * ifac[n - k] % mod


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


if x > y:
    x, y = y, x

dist = x + y

if dist % 3 != 0:
    print(0)
else:
    total = int((x + y) / 3)
    n = x - total

    if y > 2 * x:
        print(0)
    else:
        fac, ifac = make_tables(total, MOD)
        ans = nCk(total, n, fac, ifac, MOD)
        print(ans)
