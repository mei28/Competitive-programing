def search_max(l, r):
    return max(A[l:r])


def fill(l, r, height):
    for i in range(r - l):
        A[i + l] = height


if __name__ == "__main__":
    W, N = map(int, input().split())
    A = [0 for i in range(5 * 10**5 + 100)]
    LR = []
    for i in range(N):
        l, r = map(int, input().split())
        r += 1
        LR.append([l, r])
    for l, r in LR:
        height = search_max(l, r) + 1
        fill(l, r, height)
        print(height)
