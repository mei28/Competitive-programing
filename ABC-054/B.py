n, m = map(int, input().split())
A = [input() for _ in range(n)]
B = [input() for _ in range(m)]


for ia in range(n - m + 1):
    for ja in range(n - m + 1):
        flg = True
        for ib in range(m):
            for jb in range(m):
                if A[ia + ib][ja + jb] != B[ib][jb]:
                    flg = False

        if flg:
            print("Yes")
            exit()

print("No")
