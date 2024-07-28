H, W = map(int, input().split())
img1 = [list(map(int, input().split())) for _ in range(H)]
img2 = [list(map(int, input().split())) for _ in range(H)]

new_img = [[0] * (2 * W - 1) for _ in range(2 * H - 1)]

n_img1 = [[0] * (2 * W) for _ in range(2 * H)]
n_img2 = [[0] * (2 * W) for _ in range(2 * H)]

for i in range(H):
    for j in range(W):
        n_img1[2 * i][2 * j] = img1[i][j]
        n_img1[2 * i + 1][2 * j] = img1[i][j]
        n_img1[2 * i][2 * j + 1] = img1[i][j]
        n_img1[2 * i + 1][2 * j + 1] = img1[i][j]

for i in range(H):
    for j in range(W):
        n_img2[2 * i][2 * j] = img2[i][j]
        n_img2[2 * i + 1][2 * j] = img2[i][j]
        n_img2[2 * i][2 * j + 1] = img2[i][j]
        n_img2[2 * i + 1][2 * j + 1] = img2[i][j]


new_img = [[0] * (2 * W - 1) for _ in range(2 * H - 1)]

for i in range(2 * H - 1):
    for j in range(2 * W - 1):
        new_img[i][j] = (n_img1[i + 1][j + 1] + n_img2[i][j]) // 2


[print(" ".join(map(str, row))) for row in new_img]
