from sys import stderr


def score(field: list):
    return field.count(0)


t = int(input())
queries = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(t)]


WIDTH = 10000
X = [0] * 20
ans = [[0, [], [0] * 20]]


def checkA(p, q, r, field):
    ret = field.copy()
    ret[p] += 1
    ret[q] += 1
    ret[r] += 1
    return ret


def checkB(p, q, r, field):
    ret = field.copy()
    ret[p] -= 1
    ret[q] -= 1
    ret[r] -= 1
    return ret


score_sum = 0
for p, q, r in queries:
    candidates = []

    for now_score, qstr, X in ans:
        aqstr = qstr + ["A"]
        a_field = checkA(p, q, r, X)
        a_score = score(a_field)
        candidates.append([a_score + now_score, aqstr, a_field])

        bqstr = qstr + ["B"]
        b_field = checkB(p, q, r, X)
        b_score = score(b_field)
        candidates.append([b_score + now_score, bqstr, b_field])

    candidates.sort(reverse=True)
    ans = candidates[:WIDTH]


for ab in ans[0][1]:
    print(ab)

print(ans[0][0], file=stderr)
