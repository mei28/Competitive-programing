import bisect


class BIT:
    def __init__(self, n):
        self.n = len(n) if isinstance(n, list) else n
        self.size = 1 << (self.n - 1).bit_length()
        if isinstance(n, list):  # nは1-indexedなリスト
            a = [0]
            for p in n:
                a.append(p + a[-1])
            a += [a[-1]] * (self.size - self.n)
            self.d = [a[p] - a[p - (p & -p)] for p in range(self.size + 1)]
        else:  # nは大きさ
            self.d = [0] * (self.size + 1)

    def __repr__(self):
        p = self.size
        res = []
        while p > 0:
            res2 = []
            for r in range(p, self.size + 1, p * 2):
                l = r - (r & -r) + 1
                res2.append(f"[{l}, {r}]:{self.d[r]}")
            res.append(" ".join(res2))
            p >>= 1
        res.append(f"{[self.sum(p + 1) - self.sum(p) for p in range(self.size)]}")
        return "\n".join(res)

    def add(self, p, x):  # O(log(n)), 点pにxを加算
        assert p > 0
        while p <= self.size:
            self.d[p] += x
            p += p & -p

    def get(self, p, default=None):  # O(log(n))
        assert p > 0
        return (
            self.sum(p) - self.sum(p - 1)
            if 1 <= p <= self.n or default is None
            else default
        )

    def sum(self, p):  # O(log(n)), 閉区間[1, p]の累積和
        assert p >= 0
        res = 0
        while p > 0:
            res += self.d[p]
            p -= p & -p
        return res

    def lower_bound(self, x):  # O(log(n)), x <= 閉区間[1, p]の累積和 となる最小のp
        if x <= 0:
            return 0
        p, r = 0, self.size
        while r > 0:
            if p + r <= self.n and self.d[p + r] < x:
                x -= self.d[p + r]
                p += r
            r >>= 1
        return p + 1


class MultiSet:
    # n: サイズ、compress: 座圧対象list-likeを指定(nは無効)
    # multi: マルチセットか通常のOrderedSetか
    def __init__(self, n=0, *, compress=[], multi=True):
        self.multi = multi
        self.inv_compress = (
            sorted(set(compress)) if len(compress) > 0 else [i for i in range(n)]
        )
        self.compress = {k: v for v, k in enumerate(self.inv_compress)}
        self.counter_all = 0
        self.counter = [0] * len(self.inv_compress)
        self.bit = BIT(len(self.inv_compress))

    def add(self, x, n=1):  # O(log n)
        if not self.multi and n != 1:
            raise KeyError(n)
        x = self.compress[x]
        count = self.counter[x]
        if count == 0 or self.multi:  # multiなら複数カウントできる
            self.bit.add(x + 1, n)
            self.counter_all += n
            self.counter[x] += n

    def remove(self, x, n=1):  # O(log n)
        if not self.multi and n != 1:
            raise KeyError(n)
        x = self.compress[x]
        count = self.bit.get(x + 1)
        if count < n:
            raise KeyError(x)
        self.bit.add(x + 1, -n)
        self.counter_all -= n
        self.counter[x] -= n

    def __repr__(self):
        return f'MultiSet {{{(", ".join(map(str, list(self))))}}}'

    def __len__(self):  # oprator len: O(1)
        return self.counter_all

    def count(self, x):  # O(1)
        return self.counter[self.compress[x]] if x in self.compress else 0

    def __getitem__(self, i):  # operator []: O(log n)
        if i < 0:
            i += len(self)
        x = self.bit.lower_bound(i + 1)
        if x > self.bit.n:
            raise IndexError("list index out of range")
        return self.inv_compress[x - 1]

    def __contains__(self, x):  # operator in: O(1)
        return self.count(x) > 0

    def bisect_left(self, x):  # O(log n)
        return self.bit.sum(bisect.bisect_left(self.inv_compress, x))

    def bisect_right(self, x):  # O(log n)
        return self.bit.sum(bisect.bisect_right(self.inv_compress, x))


n = int(input())
q = int(input())
L = []
j_max = set()
for _ in range(q):
    l = input().split()
    L.append(l)
    if l[0] == "1":
        j_ = int(l[1])
        j_max.add(j_)
j_max_n = max(j_max)
dct = {x: i + 1 for i, x in enumerate(sorted(list(j_max)))}
rev_dct = {i + 1: x for i, x in enumerate(sorted(list(j_max)))}

for2 = [MultiSet(j_max_n + 1) for _ in range(n + 1)]
for3 = [MultiSet(n + 1, multi=False) for _ in range(j_max_n + 1)]
for l in L:
    if l[0] == "1":
        i, j = map(int, l[1:])
        i = dct[i]
        mj = for2[j]
        mj.add(i)
        mi = for3[i]
        mi.add(j)
    elif l[0] == "2":
        k = int(l[1])
        mm = for2[k]
        ans = [rev_dct[m] for m in mm]
        print(*ans)
    elif l[0] == "3":
        k = int(l[1])
        k = dct[k]
        mm = for3[k]
        print(*list(mm))
