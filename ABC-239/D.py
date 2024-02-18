a, b, c, d = map(int, input().split())


def sieve_of_eratosthenes():
    prime = [True for _ in range(210)]
    prime[0] = False
    prime[1] = False

    ret = []

    for i in range(2, 210):
        if prime[i]:
            for j in range(2 * i, 210, i):
                prime[j] = False
        if prime[i]:
            ret.append(i)
    return ret


primes = set(sieve_of_eratosthenes())
takahashi = False
for i in range(a, b + 1):
    ret = any([i + j in primes for j in range(c, d + 1)])
    if ret == False:
        takahashi = True

if takahashi:
    print("Takahashi")
else:
    print("Aoki")
