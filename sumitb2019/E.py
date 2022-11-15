n = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

r, g, b = 0, 0, 0
ans = 1
for a in A:
    ans *= [r, g, b].count(a)
    ans %= MOD

    if r == a:
        r += 1
    elif g == a:
        g += 1
    elif b == a:
        b += 1
    else:
        print(0)
        exit()
print(ans)
