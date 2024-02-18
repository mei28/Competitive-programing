n, d = map(int, input().split())

MAX = 20
imos = [0] * (MAX)

for i in range(n):
    l, r = map(lambda x: int(x), input().split())
    imos[l] += 1
    imos[r + 1] -= 1

for i in range(MAX):
    if 0 < i:
        imos[i] += imos[i - 1]

print(imos)
