N = 3
N2 = N * N


class Puzzle:
    f: list = [0] * N2
    space: int = 0
    path: str = ""

    def check(self):
        for i in range(1, N2):
            if self.f[i - 1] > self.f[i]:
                return False
        return True


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, -1]
