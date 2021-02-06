H,W = map(int,input().split())

tab = [['.' for _ in range(W)] for _ in range(H)]

for i in range(H):
    line = input()
    for j, v in enumerate(line):
        tab[i][j] = v
