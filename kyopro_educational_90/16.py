n = int(input())
a, b, c = map(int, input().split())

ans = 10000

for i in range(0, 10000):
    for j in range(0, 100000 - i):
        q = n - a * i - b * j
        k = q / c

        if i + j + k > 10000 or q < 0:
            continue
        if i + j + k < 10000 and q % c == 0:
            ans = min(ans, i + j + k)

print(ans)
