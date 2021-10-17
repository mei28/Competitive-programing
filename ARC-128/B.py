t = int(input())


for i in range(t):
    rgb = list(map(int, input().split()))
    rgb.sort()
    a, b, c = rgb
    ans = 1 << 50
    if (b - a) % 3 == 0:
        ans = min(b, ans)
    if (c - a) % 3 == 0:
        ans = min(c, ans)
    if (c - b) % 3 == 0:
        ans = min(c, ans)

    print(ans if ans != 1 << 50 else -1)
