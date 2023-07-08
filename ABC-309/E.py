import sys
from collections import deque


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    parents = [0] + list(map(int, input().split()))
    G = [[] for _ in range(N + 1)]
    for i in range(2, N + 1):
        G[parents[i - 1]].append(i)

    children = [0] + [[] for _ in range(N)]
    for i in reversed(range(1, N + 1)):
        children[i].sort(reverse=True)
        if parents[i - 1] != 0 and (
            not children[parents[i - 1]]
            or children[i][0] + 1 > children[parents[i - 1]][0]
        ):
            children[parents[i - 1]].append(children[i][0] + 1)

    insurances = [list(map(int, input().split())) for _ in range(M)]
    insurances.sort(key=lambda x: -x[1])
    covered = [0] * (N + 1)
    for x, y in insurances:
        if not children[x] or y < children[x][0]:
            children[x].append(y)
        while children[x] and children[x][-1] <= covered[x]:
            children[x].pop()
        if children[x]:
            covered[x] = max(covered[x], children[x][-1] + 1)
    print(sum([1 if c > 0 else 0 for c in covered]))


if __name__ == "__main__":
    main()
