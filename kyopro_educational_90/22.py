def gcd(m, n):
    if n == 0:
        return m
    return gcd(n, m % n)


if __name__ == "__main__":
    a, b, c = map(int, input().split())

    r = gcd(a, gcd(b, c))
    ans = (a // r - 1) + (b // r - 1) + (c // r - 1)
    print(ans)
