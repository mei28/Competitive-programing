def min_switches_to_win(N, districts):
    gains = []
    total_seats = 0

    for X, Y, Z in districts:
        if X > Y:
            total_seats += Z
        else:
            switch = (Y - X) // 2 + 1
            efficiency = Z / switch
            gains.append((efficiency, switch, Z))

    # 議席取得効率が高い順にソート
    gains.sort(key=lambda x: (-x[0], x[1]))

    half_seats = sum(Z for _, _, Z in districts) // 2 + 1
    switches_needed = 0

    for efficiency, switch, Z in gains:
        if total_seats + Z < half_seats:
            total_seats += Z
            switches_needed += switch
        else:
            # 最も鞍替えコストが少ない選挙区を選ぶ
            min_switch = min(gains, key=lambda x: x[1])[1]
            switches_needed += min_switch
            break

    return switches_needed


N = int(input())
districts = [list(map(int, input().split())) for _ in range(N)]
print(min_switches_to_win(N, districts))
