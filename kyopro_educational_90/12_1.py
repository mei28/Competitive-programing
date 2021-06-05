import sys
from typing import Iterable, List


class UnionFindTree(object):
    """Union Find Tree class"""

    __slots__ = "parent"

    def __init__(self, n: int) -> None:
        self.parent = [-1] * n

    def find(self, x: int) -> int:
        p = self.parent
        par, seq = p[x], []
        while par >= 0:
            seq.append(x)
            x, par = par, p[par]
        for c in seq:
            p[c] = x
        return x

    def union(self, x: int, y: int) -> bool:
        x, y, p = self.find(x), self.find(y), self.parent
        if x == y:
            return False
        if p[x] > p[y]:
            x, y = y, x
        p[x], p[y] = p[x] + p[y], x
        return True

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def size(self, x: int) -> int:
        return -self.parent[self.find(x)]

    def same_all(self, indices: Iterable[int]) -> bool:
        f, v = self.find, self.find(indices[0])
        return all(f(i) == v for i in indices)

    def groups(self) -> List[int]:
        return [i for i, p in enumerate(self.parent) if p < 0]


def main():
    input = sys.stdin.readline
    H, W = map(int, input().split())
    Q = int(input())
    M = [[0] * W for _ in range(H)]
    uf = UnionFindTree(H * W)

    for _ in range(Q):
        t, *p = map(int, input().split())
        if t == 1:
            x, y = p
            x, y = x - 1, y - 1
            M[x][y] = 1

            for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                # if 0 <= i < H and 0 <= j < W:
                #     uf.union(x * W + y, i * W + j)
                if i < 0 or i >= H or j < 0 or j >= W:
                    continue
                if M[i][j]:
                    uf.union(x * W + y, i * W + j)
        else:
            xa, ya, xb, yb = map(lambda x: x - 1, p)
            print("Yes" if M[xa][ya] and uf.same(xa * W + ya, xb * W + yb) else "No")


if __name__ == "__main__":
    main()
    pass
