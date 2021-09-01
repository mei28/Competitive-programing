import sys

LIM = 1000000000


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = int(input())
    x1 = 0 if s == LIM * LIM else 1
    y1 = 0
    x2 = min((s // LIM) + 1, LIM)
    y2 = s % LIM
    x3 = 0
    y3 = LIM
    print(x1, y1, x2, y2, x3, y3)


main()
