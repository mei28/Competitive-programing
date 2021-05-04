def eratos(limits: int) -> list:
    primes = []
    is_prime = [True] * (limits + 1)
    is_prime[0] = False
    is_prime[1] = False

    for p in range(0, limits + 1):
        if not is_prime[p]:
            continue
        primes.append(p)
        for i in range(p * p, limits + 1, p):
            is_prime[i] = False
    return primes


if __name__ == "__main__":
    N, K = map(int, input().split())
    ans = [0] * (N + 10)
    ans

    for i in range(2, N + 1):
        if ans[i] != 0:
            continue
        for j in range(i, N + 1, i):
            ans[j] += 1

    cnt = 0
    for a in ans:
        if a >= K:
            cnt += 1
    print(cnt)
