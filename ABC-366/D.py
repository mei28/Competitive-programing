N = int(input())

A = [[[0] * N for _ in range(N)] for _ in range(N)]

for x in range(N):
    for y in range(N):
        A[x][y] = list(map(int, input().split()))

cum_sum = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]

for x in range(1, N + 1):
    for y in range(1, N + 1):
        for z in range(1, N + 1):
            cum_sum[x][y][z] = (
                A[x - 1][y - 1][z - 1]
                + cum_sum[x - 1][y][z]
                + cum_sum[x][y - 1][z]
                + cum_sum[x][y][z - 1]
                - cum_sum[x - 1][y - 1][z]
                - cum_sum[x - 1][y][z - 1]
                - cum_sum[x][y - 1][z - 1]
                + cum_sum[x - 1][y - 1][z - 1]
            )

Q = int(input())
results = []

for _ in range(Q):
    Lx, Rx, Ly, Ry, Lz, Rz = map(int, input().split())

    result = (
        cum_sum[Rx][Ry][Rz]
        - cum_sum[Lx - 1][Ry][Rz]
        - cum_sum[Rx][Ly - 1][Rz]
        - cum_sum[Rx][Ry][Lz - 1]
        + cum_sum[Lx - 1][Ly - 1][Rz]
        + cum_sum[Lx - 1][Ry][Lz - 1]
        + cum_sum[Rx][Ly - 1][Lz - 1]
        - cum_sum[Lx - 1][Ly - 1][Lz - 1]
    )

    results.append(result)

for res in results:
    print(res)
