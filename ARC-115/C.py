n = int(input())

ans = [0] * (n + 1)


def is_prime(n: int):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    primes.append(1)

    for i in range(2, n + 1):
        if not is_prime[i]:
            continue
        primes.append(i)
        for j in range(2 * i, n + 1, i):
            is_prime[j] = False
    return set(primes)


primes = is_prime(n)

ans[1] = 1
for i in range(2, n + 1):
    if i in primes:
        ans[i] = 2

for i in range(2, n + 1):
    if i in primes:
        for k, j in enumerate(range(2 * i, n + 1, i)):
            ans[j] = i + k + 1
print(*ans[1:])
