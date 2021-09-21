import math
from typing import List


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def getangle(a: Point, b: Point) -> float:
    # a,bの偏角を求める
    ll = Point(a.x - b.x, a.y - b.y)
    if ll.y >= 0.0:
        I = ll.x / math.sqrt(ll.x * ll.x + ll.y * ll.y)
        kaku = math.acos(I) * 180.0 / math.pi
        return kaku
    else:
        I = ll.x / math.sqrt(ll.x * ll.x + ll.y * ll.y)
        kaku = math.acos(I) * 180.0 / math.pi
        return 360.0 - kaku


def getangle2(I1: float, I2: float) -> float:
    # 偏角I1 - 原点 - 偏角I2のなす角度を求める
    # I1=240, I23 = 30 -> 150

    res = abs(I1 - I2)
    if res >= 180.0:
        return 360.0 - res
    else:
        return res


# 3つの点を全探索する
def solve_slow():
    ans = 0.0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if i == j == k:
                    continue
                i1 = getangle(G[i], G[j])
                i2 = getangle(G[k], G[j])
                ans = max(ans, getangle2(i1, i2))

    print(ans)


def solve(idx: int):
    # 偏角の昇順ソートをする
    vec = []
    for i in range(N):
        if i == idx:
            continue
        angle = getangle(G[i], G[idx])
        vec.append(angle)
    vec.sort()

    ret = 0.0
    for i in range(len(vec)):
        target = vec[i] + 180.0
        if target >= 360:
            target -= 360
        pos1 = binary_search(vec, target)

        idx_1 = pos1 % len(vec)
        idx_2 = (pos1 + len(vec) - 1) % len(vec)

        candidate_1 = getangle2(vec[i], vec[idx_1])
        candidate_2 = getangle2(vec[i], vec[idx_2])
        ret = max(ret, candidate_1, candidate_2)

    return ret


def binary_search(vec: List[float], target: float):
    left = 0
    right = len(vec) - 1

    while right - left > 1:
        mid = left + (right - left) // 2
        if vec[mid] < target:
            right = mid
        else:
            left = mid

    return left


def solve_fast():
    ans = 0.0
    for i in range(N):
        ret = solve(i)
        ans = max(ret, ans)
    if int(ans) == ans:
        print(int(ans))
    else:
        print(ans)


if __name__ == "__main__":
    N = int(input())
    G = []

    for i in range(N):
        x, y = map(int, input().split())
        P = Point(x, y)
        G.append(P)
    # 全探索する時 O(N^3)だから遅い
    # solve_slow()
    solve_fast()
