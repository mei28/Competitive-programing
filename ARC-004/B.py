n = int(input())
D = [int(input()) for _ in range(n)]
print(sum(D))

if n >= 3:
    ans = 10 << 30
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            a = sum(D[:i])
            b = sum(D[i:j])
            c = sum(D[j:])

            a, c, b = sorted([a, b, c])
            if b < a + c:
                print(0)
                exit()
            else:
                ans = min(ans, b - a - c)
    print(ans)
if n == 2:
    print(abs(D[0] - D[1]))
if n == 1:
    print(D[0])
