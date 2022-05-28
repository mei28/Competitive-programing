import heapq


class Multiset:
    def __init__(self):
        self.addset = []
        self.delset = []

    def add(self, value):
        heapq.heappush(self.addset, value)

    def discard(self, value):
        heapq.heappush(self.delset, value)

    def smallest(self):
        while self.delset and self.addset[0] == self.delset[0]:
            heapq.heappop(self.addset)
            heapq.heappop(self.delset)
        return self.addset[0]

    def is_empty(self):
        return len(self.addset) - len(self.delset) <= 0


Q = int(input())

A = Multiset()
B = Multiset()
dct = {}
for _ in range(Q):
    l = list(input().split())

    if l[0] == "1":
        x = int(l[1])
        A.add(x)
        B.add(-x)
        dct[x] = dct.setdefault(x, 0) + 1

    elif l[0] == "2":
        x, c = map(int, l[1:])
        try:
            cnt = dct[x]
            d = min(c, dct[x])
            dct[x] -= d

            for _ in range(d):
                A.discard(x)
                B.discard(-x)
        except:
            continue

    else:
        # print(A.addset, B.addset, A.delset, B.delset)
        print(abs(B.smallest()) - A.smallest())
