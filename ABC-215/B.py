n = int(input())

ans = 0
now = 1
for i in range(1000000):
    if now * 2 <= n:
        ans += 1
        now *= 2
    else:
        print(ans)
        exit()
