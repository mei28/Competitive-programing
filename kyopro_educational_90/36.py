from typing import List


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x - y
        self.y = x + y


if __name__ == "__main__":
    N, Q = map(int, input().split())
    P: List[Point] = []
    for i in range(N):
        x, y = map(int, input().split())
        P.append(Point(x, y))

    min_x, min_y = 1 << 60, 1 << 60
    max_x, max_y = -1 << 60, -1 << 60

    for p in P:
        min_x = min(min_x, p.x)
        min_y = min(min_y, p.y)
        max_x = max(max_x, p.x)
        max_y = max(max_y, p.y)

    for _ in range(Q):
        idx = int(input()) - 1
        p = P[idx]
        ret1 = abs(max_x - p.x)
        ret2 = abs(max_y - p.y)
        ret3 = abs(min_x - p.x)
        ret4 = abs(min_y - p.y)
        print(max([ret1, ret2, ret3, ret4]))
