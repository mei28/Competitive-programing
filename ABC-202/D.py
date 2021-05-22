a, b, k = map(int, input().split())
n = a + b

c = 0
ans = ""
for bit in range((1 << a) - 1, 2 ** n):
    cnt = 0
    ans = ""
    for j in range(n):
        if (bit >> j) & 1:
            cnt += 1
            ans = "b" + ans
        else:
            ans = "a" + ans
    if cnt == a:
        print(ans)
        c += 1
    if c == k:
        break

print(ans)
