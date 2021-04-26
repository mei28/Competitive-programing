import math

PI = math.pi


def query(e):
    cx = 0
    cy = -(l / 2) * math.sin(e / t * 2 * PI)
    cz = (l / 2) - (l / 2) * math.cos(e / t * 2 * PI)

    d1 = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))
    d2 = cz

    kaku = math.atan2(d2, d1)
    return kaku * 180 / PI


if __name__ == "__main__":
    t = int(input())
    l, x, y = map(int, input().split())
    q = int(input())

    E = [int(input()) for _ in range(q)]

    for e in E:
        print(f"{query(e):.20f}")
