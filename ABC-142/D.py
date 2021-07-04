from itertools import combinations
from typing import List


def prime_factoraization(n: int) -> List[int]:
    li = []

    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            li.append(i)
            n /= i

    if n > 1:
        li.append(int(n))
    return li


if __name__ == "__main__":
    a, b = map(int, input().split())
    prime_a = prime_factoraization(a)
    prime_b = prime_factoraization(b)

    ans = len(set(prime_a) & set(prime_b)) + 1
    print(ans)
