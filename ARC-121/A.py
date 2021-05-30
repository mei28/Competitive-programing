class Point:
    def __init__(self, x: int, y: int, idx: int):
        self.x = x
        self.y = y
        self.idx = idx

    def __str__(self):
        return f"{ self.x }, { self.y }, { self.idx }"


def calc_diff(p1: Point, p2: Point) -> int:
    if p1.idx == p2.idx:
        return -1
    return max(abs(p1.x - p2.x), abs(p1.y - p2.y))


if __name__ == "__main__":
    N = int(input())
    points = []
    for i, _ in enumerate(range(N)):
        x, y = map(int, input().split())
        p = Point(x, y, i)
        points.append(p)

    points_x = list(sorted(points, key=lambda x: x.x))
    points_y = list(sorted(points, key=lambda x: x.y))
    if N >= 10:
        tmp = set()
        for i in range(4):
            tmp.add(points_x[i].idx)
            tmp.add(points_x[-i - 1].idx)
            tmp.add(points_y[i].idx)
            tmp.add(points_y[-i - 1].idx)
    else:
        tmp = [i for i in range(N)]

    ans = []
    for i in tmp:
        for j in tmp:
            if i <= j:
                continue
            p1 = points[i]
            p2 = points[j]

            diff = calc_diff(p1, p2)
            if diff != -1:
                ans.append(diff)

    ans.sort(reverse=True)
    print(ans[1])
