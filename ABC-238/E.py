from typing import List


class UnionFind:
    """0-index"""

    def __init__(self, n: int):
        self.n = n
        self.parent = [-1] * n
        self.__group_count = n

    def unite(self, x: int, y: int) -> bool:
        """merge x and y"""
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        self.__group_count -= 1

        if self.parent[x] > self.parent[y]:
            x, y = y, x

        self.parent[x] += self.parent[y]
        self.parent[y] = x

        return True

    def is_same(self, x: int, y: int) -> bool:
        """check x and y is same group"""
        return self.root(x) == self.root(y)

    def root(self, x: int) -> int:
        """get the root of x"""
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def size(self, x) -> int:
        return -self.parent[self.root(x)]

    def all_sizes(self) -> List[int]:
        sizes = []
        for i in range(self.n):
            size = self.parent[i]
            if size < 0:
                sizes.append(-size)
        return sizes

    @property
    def group_count(self) -> int:
        return self.__group_count


def solve():
    n, q = map(int, input().split())
    uf = UnionFind(n + 1)
    for _ in range(q):
        a, b = map(int, input().split())
        uf.unite(a - 1, b)

    return uf.is_same(0, n)


print("Yes" if solve() else "No")
