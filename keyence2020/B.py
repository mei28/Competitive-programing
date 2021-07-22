n = int(input())
X, L = [], []
XLs = []
for i in range(n):
    x, l = map(int, input().split())
    XLs.append([x, l, x + l])
XLs = list(sorted(XLs, key=lambda x: x[2]))

choice = -(10 ** 10)
cnt = 0
for i in range(n):
    x = XLs[i][0]
    l = XLs[i][1]

    if choice <= x - l:
        choice = x + l
        cnt += 1
print(cnt)
