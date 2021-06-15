from collections import Counter


def solve(l: str):
    ac = Counter(l[::2]).most_common(2)
    bc = Counter(l[1::2]).most_common(2)

    if ac[0][0] != bc[0][0]:
        return n - ac[0][1] - bc[0][1]
    else:
        if len(bc) == 1 or len(ac) == 1:
            return n // 2
        else:
            return n - max(ac[0][1] + bc[1][1], ac[1][1] + bc[0][1])


if __name__ == "__main__":
    n = int(input())
    l = input()
    print(solve(l.split(" ")))
