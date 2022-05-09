n, a, b = map(int, input().split())


ans = [["." for _ in range(b * n)] for _ in range(a * n)]


def re(i: int, j: int, flg):
    for n in range(a):
        for m in range(b):
            if flg:
                ans[i * a + n][m + j * b] = "."
            else:
                ans[i * a + n][m + j * b] = "#"


for i in range(n):
    flg = i % 2 == 0
    for j in range(n):
        re(i, j, flg)
        flg = not flg

for f in ans:
    print("".join(f))
