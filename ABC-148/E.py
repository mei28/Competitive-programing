n = int(input())

if n % 2 != 0:
    print(0)
else:
    n //= 2
    ans = 0
    while n > 0:
        ans += n // 5
        n //= 5
    print(ans)
