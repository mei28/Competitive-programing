n, m = map(int, input().split())


class Player:
    def __init__(self, id: int, hands: str):
        self.id: int = id
        self.hands: str = hands
        self.num_win: int = 0


players = []

for i in range(2 * n):
    _hand = input()
    players.append(Player(i + 1, _hand))

winner = []
loser = []


def judge(a, b, j):
    hand_a = a.hands[j]
    hand_b = b.hands[j]

    if hand_a == "G" and hand_b == "C":
        return 1, 0
    if hand_a == "C" and hand_b == "P":
        return 1, 0
    if hand_a == "P" and hand_b == "G":
        return 1, 0
    if hand_a == "G" and hand_b == "G":
        return 0, 0
    if hand_a == "C" and hand_b == "C":
        return 0, 0
    if hand_a == "P" and hand_b == "P":
        return 0, 0
    else:
        return 0, 1


for i in range(m):
    for j in range(0, 2 * n, 2):
        a, b = players[j], players[j + 1]
        judge_a, judge_b = judge(a, b, i)
        a.num_win += judge_a
        b.num_win += judge_b

    players = list(sorted(players, key=lambda x: (-x.num_win, x.id)))

for i in players:
    print(i.id)
