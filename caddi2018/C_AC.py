from collections import Counter

N, P = map(int, input().split())

primes = Counter()
for denominator in range(2, int(P ** 0.5) + 1):
    while P % denominator == 0:
        P //= denominator
        primes[denominator] += 1
primes[P] += 1

ans = 1
for p in primes.keys():
    while primes[p] >= N:
        ans *= p
        primes[p] -= N

print(ans)
