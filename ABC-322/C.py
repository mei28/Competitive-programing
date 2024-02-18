def find_next_firework(day, firework_days):
    low, high = 0, len(firework_days) - 1

    while low <= high:
        mid = (low + high) // 2

        if firework_days[mid] == day:
            return 0
        elif firework_days[mid] < day:
            low = mid + 1
        else:
            high = mid - 1

    return firework_days[low] - day


def main():
    N, M = map(int, input().split())
    firework_days = list(map(int, input().split()))

    for i in range(1, N + 1):
        print(find_next_firework(i, firework_days))


if __name__ == "__main__":
    main()
