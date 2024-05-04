n = int(input())
AB = [list(map(int, input().split())) for _ in range(n)]


def max_height(N, giants):
    giants.sort(key=lambda x: x[1] - x[0])

    total_height = 0
    max_head_height = 0

    for A, B in giants:
        current_head_height = total_height + B
        if current_head_height > max_head_height:
            max_head_height = current_head_height
        total_height += A

    return max_head_height


print(max_height(n, AB))
