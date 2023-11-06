import random
from collections import defaultdict

n, m = map(int, input().split())
piles = [list(map(int, input().split())) for _ in range(m)]
piles.insert(0, [])


def show_piles():
    print("---")
    for p in piles:
        print(p)
    print("---")


def choice_to(fr):
    pile_heights = defaultdict(set)
    min_height = float("inf")

    for i in range(1, m + 1):
        if fr == i:
            continue
        height = len(piles[i])
        pile_heights[height].add(i)
        min_height = min(min_height, height)

    return random.choice(list(pile_heights[min_height]))


def move_pile(target_idx, fr):
    idx = piles[fr].index(target_idx)

    if idx == len(piles[fr]) - 1:
        print(f"{target_idx} {0}")
        piles[fr] = piles[fr][:-1]
        return
    else:
        move_pile = piles[fr][idx + 1 :]
        piles[fr] = piles[fr][:idx]
        to = choice_to(fr)
        print(f"{move_pile[0]} {to}")
        piles[to] += move_pile

        print(f"{target_idx} {0}")
    # show_piles()


target_idx = 1
while target_idx <= n:
    for fr in range(1, m + 1):
        if target_idx in piles[fr]:
            move_pile(target_idx, fr)
            target_idx += 1
