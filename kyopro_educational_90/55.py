from itertools import combinations

n, p, q = map(int, input().split())
A = list(map(int, input().split()))
A = list(map(lambda x: x % p, A))

ans = sum(
    1 for a, b, c, d, e in combinations(A, 5) if a * b % p * c % p * d % p * e % p == q
)

print(ans)
