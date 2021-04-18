class UnionFind:
    def __init__(self, sz):
        self.n = sz
        self.par = [-1] * sz

    def root(self, pos: int) -> int:
        if self.par[pos] < 0:
            return pos
        self.par[pos] = self.root(self.par[pos])
        return self.par[pos]

    def unite(self, u: int, v: int) -> None:
        u = self.root(u)
        v = self.root(v)
        if u == v:
            return
        self.par[u] = v

    def same(self, u: int, v: int) -> bool:
        if self.root(u) == self.root(v):
            return True
        return False


def query1(px: int, py: int):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        sx = px + dx[i]
        sy = py + dy[i]
        if not used[sx][sy]:
            continue
        hash1 = (px - 1) * W + (py - 1)
        hash2 = (sx - 1) * W + (sy - 1)
        UF.unite(hash1, hash2)
    used[px][py] = True


def query2(px: int, py: int, qx: int, qy: int):
    if not used[px][py] or not used[qx][qy]:
        return False
    hash1 = (px - 1) * W + (py - 1)
    hash2 = (qx - 1) * W + (py - 1)
    if UF.same(hash1, hash2):
        return True
    return False


if __name__ == "__main__":

    H, W = map(int, input().split())
    Q = int(input())
    Qs = [list(map(int, input().split())) for _ in range(Q)]
    # Qs = []
    # for i in range(Q):
    #     Qs.append(list(map(int, input().split())))
    UF = UnionFind(H * W)
    used = [[0 for _ in range(1009)] for _ in range(10009)]

    for q in Qs:
        if q[0] == 1:
            query1(q[1], q[2])
        else:
            ans = query2(q[1], q[2], q[3], q[4])
            if ans:
                print("Yes")
            else:
                print("No")
