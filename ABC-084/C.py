n = int(input())
stations = [list(map(int, input().split())) for _ in range(n - 1)]


def get_cost(st: int, time: int) -> int:
    # nについたらその時間を返す
    if st == n - 1:
        return time

    c, s, f = stations[st]

    # 始発
    if time <= s:
        next_train = s
    else:
        late = time % f
        if late == 0:
            next_train = time
        else:
            next_train = time + f - late

    return get_cost(st + 1, next_train + c)


for i in range(n):
    print(get_cost(i, 0))
