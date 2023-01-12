n = int(input())

MOD = 10000

ans = 0
for _ in range(n):
    t, a = input().split()
    a = int(a)

    if t == "+":
        ans += a
    if t == "-":
        ans -= a
    if t == "*":
        ans *= a
    ans %= MOD
    print(ans)
