import math
import sys


class Mat:
    def __init__(self, mat, l):
        self.mat = mat
        self.mat[0][0] = 0
        self.l = l
        self.mat[self.l][self.l] = 1

    def write_line(self, s, g):
        sx, sy = s[0], s[1]
        gx, gy = g[0], g[1]

        if gx - sx != 0:
            a = (gy - sy) / (gx - sx)

            for nx in range(min(gx, sx), max(gx, sx) + 1):
                upper_y = math.ceil(a * (nx - sx) + sy)
                lower_y = math.floor(a * (nx - sx) + sy)
                self.mat[upper_y][nx] = 9
                self.mat[lower_y][nx] = 9

        else:
            for ny in range(min(gy, sy), max(sy, gy) + 1):
                self.mat[ny][sx] = 9

    def search(self):
        pos = [[0, 0]]

        mat = self.mat
        while len(pos) > 0:
            y, x = pos.pop(0)

            if mat[y][x] == 1:
                return True
            mat[y][x] = 4

            if mat[y - 1][x] < 2 and (0 <= y - 1 < self.l):
                pos.append([y - 1, x])
            if mat[y + 1][x] < 2 and (0 <= y + 1 < self.l):
                pos.append([y + 1, x])
            if mat[y][x - 1] < 2 and (0 <= x - 1 < self.l):
                pos.append([y, x - 1])
            if mat[y][x + 1] < 2 and (0 <= x + 1 < self.l):
                pos.append([y, x + 1])
        return False


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    N, l = map(float, lines[0].split())
    N = int(N)
    l = int(l * 100) + 1
    # mat: 0は到達可能, 9は線がついている
    mat = [[0 for _ in range(l)] for _ in range(l)]

    maze_mat = Mat(mat, l - 1)

    for i in range(N):
        sx, sy, gx, gy = map(float, lines[i + 1].split())
        sx = int(100 * sx)
        sy = int(100 * sy)
        gx = int(100 * gx)
        gy = int(100 * gy)

        maze_mat.write_line((sx, sy), (gx, gy))
        if not maze_mat.search():
            print("NO")
            print(i)
            exit()

    print("YES")


if __name__ == "__main__":
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip("\r\n"))
    main(lines)
