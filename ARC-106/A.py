N = int(input())

for i in range(1, 50):
    for j in range(1, 50):
        if 3**i + 5**j == N:
            print(i, j)
            flg = False
            exit()

print(-1)
