n, k = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(n)]
AB = sorted(AB, key=lambda x: x[0])
A, B = zip(*AB)
ABC = [[1, sum(B)]]

for a, b in AB:
    last = ABC[-1]
    ABC.append([a + 1, last[1] - b])

for a, b in ABC:
    if b <= k:
        print(a)
        exit()
