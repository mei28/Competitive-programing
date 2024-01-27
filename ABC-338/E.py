class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


def has_intersection(N, cords):
    pairs = sorted((min(a, b), max(a, b)) for a, b in cords)

    bit = BIT(2 * N)

    for a, b in pairs:
        if bit.sum(b) - bit.sum(a) > 0:
            return True
        bit.add(b, 1)

    return False


N = int(input())
cords = [tuple(map(int, input().split())) for _ in range(N)]
print("Yes" if has_intersection(N, cords) else "No")
