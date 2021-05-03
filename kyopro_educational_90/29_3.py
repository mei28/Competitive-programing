from typing import List


class SegmentTree:
    def __init__(self, N: int):
        self.sz: int = 1
        while self.sz < N:
            self.sz *= 2
        self.seg: List[int] = [0] * (2 * self.sz)
        self.lazy: List = [0] * (2 * self.sz)

    def _push(self, k: int):
        if k < self.sz:
            self.lazy[k * 2] = max(self.lazy[k * 2], self.lazy[k])
            self.lazy[k * 2 + 1] = max(self.lazy[k * 2 + 1], self.lazy[k])
        self.seg[k] = max(self.seg[k], self.lazy[k])
        self.lazy[k] = 0

    def _update(self, a: int, b: int, x: int, k: int, l: int, r: int):
        self._push(k)
        if r <= a or b <= l:
            return
        if a <= l and r <= b:
            self.lazy[k] = x
            self._push(k)
            return
        self._update(a, b, x, k * 2, l, (l + r) >> 1)
        self._update(a, b, x, k * 2 + 1, (l + r) >> 1, r)
        self.seg[k] = max(self.seg[k * 2], self.seg[k * 2 + 1])

    def _range_max(self, a: int, b: int, k: int, l: int, r: int) -> int:
        self._push(k)
        if r <= a or b <= l:
            return 0
        if a <= l and r <= b:
            return self.seg[k]

        lc = self._range_max(a, b, k * 2, l, (l + r) >> 1)
        rc = self._range_max(a, b, k * 2 + 1, (l + r) >> 1, r)
        return max(lc, rc)

    def update(self, l: int, r: int, x: int):
        return self._update(l, r, x, 1, 0, self.sz)

    def range_max(self, l: int, r: int) -> int:
        return self._range_max(l, r, 1, 0, self.sz)


if __name__ == "__main__":
    W, N = map(int, input().split())
    seg_tree = SegmentTree(W)

    for i in range(N):
        l, r = map(int, input().split())
        height = seg_tree.range_max(l - 1, r) + 1
        seg_tree.update(l - 1, r, height)
        print(height)
