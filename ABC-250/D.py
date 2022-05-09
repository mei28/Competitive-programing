n = int(input())

q_max = 10**6 + 10


def get_primes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    for p in range(0, limit + 1):
        if not is_prime[p]:
            continue
        primes.append(p)
        for i in range(p * p, limit + 1, p):
            is_prime[i] = False
    primes.sort()
    return primes


primes = get_primes(q_max)

ans = 0

for i in range(len(primes)):
    t = primes[i] **3
    for j in range(i):
        if t*primes[j]>n:
            break
        ans += 1

print(ans)
