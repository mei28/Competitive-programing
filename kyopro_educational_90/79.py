from typing import List


def is_same(_A: List[List[int]], _B: List[List[int]]) -> bool:
    for a, b in zip(_A, _B):
        if a != b:
            return False
    return True


def show(_A: List[List[int]]) -> None:
    print("-" * 20)
    for a in _A:
        print(*a)
    print("-" * 20)


if __name__ == "__main__":
    dx = [0, 0, 1, 1]
    dy = [0, 1, 0, 1]

    h, w = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(h)]
    B = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0
    for i in range(h - 1):
        for j in range(w - 1):
            diff = B[i][j] - A[i][j]
            cnt += abs(diff)
            for nx, ny in zip(dx, dy):
                A[i + nx][j + ny] += diff

    if is_same(A, B):
        print("Yes")
        print(cnt)
    else:
        print("No")
