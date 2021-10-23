n = int(input())

ans = 1 << 50
for h in range(1, int(n ** 0.5) + 1):
    w = n // h
    amari = n % h

    _tmp = abs(h - w) + amari
    ans = min(ans, _tmp)

print(ans)
