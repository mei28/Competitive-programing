N = int(input())

# get prime numbers
def eratos(N):
    prime = [True] * (N + 1)
    prime[0] = False
    prime[1] = False
    for i in range(2, int(N**0.5) + 1):
        if prime[i]:
            for j in range(i * i, N + 1, i):
                prime[j] = False
    return [i for i in range(N + 1) if prime[i]]


primes = eratos(int(N**0.5) + 1)


cnt = set()
for i in range(len(primes) - 2):
    a = primes[i]
    if a * a > N:
        break
    for j in range(i + 1, len(primes) - 1):
        b = primes[j]
        if a * a * b > N:
            break
        for k in range(j + 1, len(primes)):
            c = primes[k]
            if a * a * b * c * c > N:
                break
            cnt.add(a * a * b * c * c)
print(len(cnt))
