import math

A, B = map(int, input().split())


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


dct = {}
for i in range(A, B + 1):
    tmp = set(make_divisors(i))
    for t in tmp:
        dct[t] = dct.setdefault(t, 0) + 1

ans = 1
for k, v in dct.items():
    if v >= 2:
        ans = max(ans, k)

print(ans)
