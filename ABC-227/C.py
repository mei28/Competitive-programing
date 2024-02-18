n = int(input())

if n == 1:
    print(1)
    exit()
ans = 0
for i in range(1, int(n**0.5)):
    for j in range(i, int(n**0.5) + 1):
        k = n // (i * j)
        if k < j:
            break
        ans += k - j + 1

print(ans)
