from collections import Counter

n, p = map(int, input().split())


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


primes = prime_factorize(p)
if len(primes) == 0:
    print(1)
    exit()

yakusuu = []
for pr in primes:
    if p % pr == 0:
        while p % pr == 0:
            p /= pr
            yakusuu.append(pr)

cnt = Counter(yakusuu)

ans = 1
for k, v in cnt.items():
    if v >= n:
        ans *= k * (v // n)

print(ans)
