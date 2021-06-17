n, k = map(int, input().split())
MOD = 1000000007


def pow(x: int, n: int) -> int:
    ret: int = 1

    while n > 0:
        if n & 1:
            ret *= x
            ret %= MOD
        x *= x
        x %= MOD
        n >>= 1
    return ret


if n == 1:
    print(k % MOD)
elif n == 2:
    print((k * (k - 1)) % MOD)
else:
    tmp = (k * (k - 1)) % MOD
    n -= 2
    p = pow(k - 2, n)
    tmp *= p
    tmp %= MOD
    print(tmp)
