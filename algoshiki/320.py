n = int(input())

for i in range(n, 0, -1):
    flg = all(i % j != 0 for j in range(2, min(int(i**0.5) + 1, n - 1)))
    if flg:
        print(i)
        exit()
