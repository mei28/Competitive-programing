#####疑似マルチセット QuasiMultiset#####
from heapq import heappop, heappush
from collections import defaultdict


class QuasiMultiset:
    def __init__(self, deleteFlag=True):
        self.len = 0
        self.f = defaultdict(int)
        self.pos = []
        self.neg = []
        self.deleteFlag = deleteFlag

    def _delete(self, key):
        if self.deleteFlag and self.f[key] == 0:
            del self.f[key]

    def add(self, x, key=None):
        if key is None:
            key = x
        self.len += 1
        heappush(self.pos, (x, key))
        heappush(self.neg, (-x, key))
        self.f[key] += 1

    def popMax(self, returnKey=False):
        while True:
            x, key = heappop(self.neg)
            if self.f[key]:
                self.f[key] -= 1
                self.len -= 1
                self._delete(key)
                if returnKey:
                    return -x, key
                else:
                    return x

    def popMin(self, returnKey=False):
        while True:
            x, key = heappop(self.pos)
            if self.f[key]:
                self.f[key] -= 1
                self.len -= 1
                self._delete(key)
                if returnKey:
                    return x, key
                else:
                    return x

    def seachMax(self, returnKey=False):
        while True:
            x, key = self.neg[0]
            if self.f[key]:
                if returnKey:
                    return -x, key
                else:
                    return -x
            else:
                heappop(self.neg)

    def seachMin(self, returnKey=False):
        while True:
            x, key = self.pos[0]
            if self.f[key]:
                if returnKey:
                    return x, key
                else:
                    return x
            else:
                heappop(self.pos)

    def deleteKey(self, key):
        self.f[key] -= 1
        self._delete(key)
        self.len -= 1

    def exist(self, key):
        if self.f.get(key) is None:
            return False
        else:
            return True


n, q = map(int, input().split())

A = QuasiMultiset()
for i in range(1, n + 1):
    A.add(i)
B = QuasiMultiset()

for _ in range(q):
    l = input().split()

    if l[0] == "1":
        x = A.popMin()
        B.add(x)
    if l[0] == "2":
        x = int(l[1])
        B.deleteKey(x)
        pass
    if l[0] == "3":
        x = B.seachMin()
        print(x)
