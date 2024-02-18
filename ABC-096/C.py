H, W = map(int, input().split())

S = [[0 for _ in range(W)] for _ in range(H)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
for i in range(H):
    s = input()
    for j in range(W):
        S[i][j] = s[j]


for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            continue
        is_can = False
        for d in range(len(dx)):
            if i + dy[d] < 0 or H <= i + dy[d] or j + dx[d] < 0 or W <= j + dx[d]:
                continue
            elif S[i + dy[d]][j + dx[d]] == "#":
                is_can = True
                break

        if is_can == False:
            print("No")
            exit()

print("Yes")
