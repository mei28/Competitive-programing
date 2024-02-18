N, M = map(int, input().split())
mat = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    line = input()
    for idx, j in enumerate(line):
        mat[i][idx] = j

dic = {"E": (0, 1), "S": (1, 0), "W": (0, -1), "N": (-1, 0), "#": (0, 0)}


def show(mat):
    for i in mat:
        print(i)

    print("-" * 20)


def cnt_ans(mat):
    ans = 0
    for i in mat:
        ans += i.count("#")
    return ans


now_y, now_x = 0, 0
for cnt in range(N * M + 1):
    dj, di = dic[mat[now_y][now_x]]
    mat[now_y][now_x] = "#"
    if now_y + dj < 0 or now_x + di < 0 or now_y + dj >= N or now_x + di >= M:
        break
    now_y += dj
    now_x += di

print(cnt_ans(mat))
