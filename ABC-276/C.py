n = int(input())
P = list(map(int, input().split()))

j = n - 2
while P[j] < P[j + 1]:
    j -= 1

k = n - 1
while P[j] < P[k]:
    k -= 1

P[j], P[k] = P[k], P[j]

print(*P[: j + 1], *P[:j:-1])
