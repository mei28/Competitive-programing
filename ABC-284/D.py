import math
from collections import Counter
from functools import lru_cache
from os import wait


# 素因数分解を行う関数
@lru_cache(maxsize=None)
def prime_factorization(n):
    # 素数で割り切れるかの判定
    for p in range(2, int(n**0.5)):
        if n % p == 0:
            if n % (p * p) == 0:
                return p, n // (p * p)
            else:
                return int((n // p) ** 0.5), p


t = int(input())


for _ in range(t):
    n = int(input())
    a, b = prime_factorization(n)
    print(a, b)
