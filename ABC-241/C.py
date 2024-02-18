n = int(input())

board = [input() for _ in range(n)]

for i in range(n):
    for j in range(n - 6 + 1):
        row = board[i][j : j + 6]
        if row.count("#") >= 4:
            print("Yes")
            exit()

for i in range(n):
    for j in range(n - 6 + 1):
        col = []
        for k in range(6):
            col.append(board[j + k][i])
            if col.count("#") >= 4:
                print("Yes")
                exit()


for i in range(n - 6 + 1):
    for j in range(n - 6 + 1):
        tmp = []
        for k in range(6):
            tmp.append(board[i + k][j + k])
        if tmp.count("#") >= 4:
            print("Yes")
            exit()
for i in range(n - 6 + 1):
    for j in range(n - 6 + 1):
        tmp = []
        for k in range(6):
            tmp.append(board[i + (5 - k)][j + k])
        if tmp.count("#") >= 4:
            print("Yes")
            exit()

print("No")
