def search_max(l, r):
    return max(h[l:r])


def fill(l, r, height):
    for i in range(r - l):
        h[i + l] = height


if __name__ == "__main__":
    W, N = map(int, input().split())
    L, R = [], []
    for i in range(N):
        l, r = map(int, input().split())
        r += 1
        L.append(l)
        R.append(r)
    compression = []
    for i in range(N):
        compression.append(L[i])
        compression.append(R[i])

    # 座標圧縮, 新しくインデックスを振り直すイメージ
    # 空白の部分に意味はないから座標を圧縮したい
    compression = list(set(compression))
    compression.sort()

    for i in range(N):
        L[i] = compression.index(L[i])
        R[i] = compression.index(R[i])

    h = [0] * len(compression)

    for i in range(N):
        height = search_max(L[i], R[i]) + 1
        fill(L[i], R[i], height)
        print(height)
