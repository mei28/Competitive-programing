def count_zoro_dates(N, D):
    # List of possible "zoro" dates (days and months with the same digit)
    zoro = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]

    dct = {
        1: [1, 11],
        2: [2, 22],
        3: [3, 33],
        4: [4, 44],
        5: [5, 55],
        6: [6, 66],
        7: [7, 77],
        8: [8, 88],
        9: [9, 99],
        11: [1, 11],
        22: [2, 22],
        33: [3, 33],
        44: [4, 44],
        55: [5, 55],
        66: [6, 66],
        77: [7, 77],
        88: [8, 88],
        99: [9, 99],
    }

    # Counter for "zoro" dates
    cnt = 0

    # Iterate over each month
    for i in range(1, N + 1):
        # Check if the month itself is a "zoro" number
        if i in zoro:
            # Check each day in the month
            for j in range(1, D[i - 1] + 1):
                # If the day is a "zoro" number, increment the counter
                if j in dct[i]:
                    cnt += 1

    return cnt


n = int(input())
D = list(map(int, input().split()))

print(count_zoro_dates(n, D))
