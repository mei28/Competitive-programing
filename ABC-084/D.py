from typing import List

q = int(input())

LR: List[List[int]] = []

_MAX = -10
for _ in range(q):
    l, r = map(int, input().split())
    LR.append([l, r])
    _MAX = max(_MAX, r)

_MAX += 10


def get_primes():
    primes: List[int] = []
    is_prime: List[bool] = [True] * (_MAX + 1)
    is_prime[0] = False
    is_prime[1] = False

    for p in range(0, _MAX + 1):
        if not is_prime[p]:
            continue

        primes.append(p)

        for i in range(p * p, _MAX + 1, p):
            is_prime[i] = False

    return primes


primes = get_primes()


def is_like_2017() -> List[int]:
    A = [0] * (_MAX)

    for i in range(0, _MAX):
        if i in primes and (i + 1) // 2 in primes:
            A[i] = 1

    return A


A = is_like_2017()

S = [0] * (_MAX + 1)

for i in range(_MAX):
    S[i + 1] = S[i] + A[i]


for l, r in LR:
    print(S[r + 1] - S[l])
    pass
