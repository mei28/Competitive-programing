def mod_pow(a: int, b: int, m: int) -> int:
    p: int = 1
    q: int = a

    for i in range(30):
        if b & (1 << i) != 0:
            p *= q
            q %= m
        q *= q
        q %= m
    return p


def div(a: int, b: int, m: int) -> int:
    # get the value of a/b
    return (a * mod_pow(b, m - 2, m)) % m


def init():
    # calculate 10^i
    power10[0] = 1
    for i in range(1, 22):
        power10[i] = 10 * power10[i - 1]


def f(x: int) -> int:
    v1 = x % MOD
    v2 = (x + 1) % MOD
    v = v1 * v2 % MOD
    return div(v, 2, MOD)


if __name__ == "__main__":
    l, r = map(int, input().split())
    MOD = 1000000007
    power10 = [0] * 25
    init()

    ans = 0
    for i in range(1, 20):
        vl = max(l, power10[i - 1])
        vr = min(r, power10[i] - 1)

        if vl > vr:
            continue
        val = (f(vr) - f(vl - 1) + MOD) % MOD
        ans += i * val
        ans %= MOD
    print(ans)
