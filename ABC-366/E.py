from bisect import bisect_left, bisect_right


def count_valid_pairs(N, D, points):
    x_points = sorted(x for x, y in points)
    y_points = sorted(y for x, y in points)

    x_cumsum = [0] * (N + 1)
    y_cumsum = [0] * (N + 1)

    for i in range(N):
        x_cumsum[i + 1] = x_cumsum[i] + x_points[i]
        y_cumsum[i + 1] = y_cumsum[i] + y_points[i]

    def sum_distance(x, y):
        x_pos = bisect_left(x_points, x)
        y_pos = bisect_left(y_points, y)

        x_dist = (
            x_pos * x
            - x_cumsum[x_pos]
            + (x_cumsum[N] - x_cumsum[x_pos])
            - (N - x_pos) * x
        )
        y_dist = (
            y_pos * y
            - y_cumsum[y_pos]
            + (y_cumsum[N] - y_cumsum[y_pos])
            - (N - y_pos) * y
        )

        return x_dist + y_dist

    count = 0
    for x in range(x_points[0] - D, x_points[-1] + D + 1):
        for y in range(y_points[0] - D, y_points[-1] + D + 1):
            if sum_distance(x, y) <= D:
                count += 1

    return count


N, D = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(N)]
result = count_valid_pairs(N, D, points)
print(result)
