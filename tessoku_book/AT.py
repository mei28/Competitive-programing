from random import randint
from time import time

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]


def dist(i, j):
    x1, y1 = points[i]
    x2, y2 = points[j]
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def score(path: list):
    res = 0
    for i in range(n):
        res += dist(path[i - 1], path[i])
    return res


base_ms = 0


def tic():
    global base_ms
    base_ms = time()


def toc():
    now = time()
    return (now - base_ms) * 1000


# init solutions
sol = list(range(n))
sol_score = score(sol)
best = sol
best_score = sol_score


def nxt(path):
    a = randint(0, n - 1)
    b = (a + randint(1, n - 1)) % n
    if a > b:
        b, a = a, b
    new_path = path[:]
    # chagne
    new_path[a:b] = path[a:b][::-1]
    return new_path


tic()

while toc() < 800:
    candidate = nxt(sol)
    candidate_score = score(candidate)
    if (
        candidate_score < sol_score
        or randint(0, 1000000000) < (900 - int(toc())) ** 2
    ):
        sol = candidate
        sol_score = candidate_score
        if sol_score < best_score:
            best = sol
            best_score = sol_score

zero = 0
while best[zero] != 0:
    zero += 1
for i in range(n + 1):
    print(best[(zero + i) % n] + 1)
print(sol_score)
