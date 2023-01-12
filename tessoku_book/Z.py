q = int(input())
X = [int(input()) for _ in range(q)]
max_X = max(X)


def eratos(x: int):
    is_primes = [True] * (x + 1)
    primes = set()

    for i in range(2, x + 1):
        if not is_primes[i]:
            continue
        primes.add(i)
        for j in range(i * i, x + 1, i):
            is_primes[j] = False
    return primes


primes = eratos(max_X)

for x in X:
    print("Yes" if x in primes else "No")
