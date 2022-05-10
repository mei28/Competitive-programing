n = int(input())


def pr(n):
    is_prime = [True] * (n + 1)
    prime = []
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, n + 1):
        if not is_prime[i]:
            continue
        prime.append(i)
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

    return prime


prime = pr(n)

for i in range(len(prime)):
    for j in range(len(prime)):
        p = prime[i]
        q = prime[j]
        if p + q == n:
            print(p)
            exit()

print(-1)
