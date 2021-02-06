def show_ans(ans):
    for i in ans:
        print(''.join(i))


def convert_1d_to_2d(l, cols):
    return [l[i:i+cols] for i in range(0, len(l), cols)]

if __name__ == '__main__':

    N, H, W, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))

    team = [0] * len(A)

    for i, a in enumerate(A):
        # チーム名を付与
        team[i] = (a, chr(ord('A')+i))

    seats = [['.']*W for _ in range(H)]

    for i in range(H):
        line = input()
        for j, l in enumerate(line):
            seats[i][j] = l

    team = sorted(team, key=lambda x: x[0], reverse=True)
    flatten_seats = sum(seats, [])

    for num, team in team:
        max_idx = flatten_seats.index(max(flatten_seats))
        if num < max_idx:
            flatten_seats[max_idx] = team

    show_ans(convert_1d_to_2d(flatten_seats, W))
