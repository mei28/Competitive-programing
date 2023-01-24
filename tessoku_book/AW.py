from sys import stderr


def score(field: list):
    return field.count(0)


t = int(input())
queries = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(t)]


X = [0] * 20
ans = []


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
    a_field = checkA(p, q, r, X)
    a_score = score(a_field)
    b_field = checkB(p, q, r, X)
    b_score = score(b_field)

    if a_score >= b_score:
        ans.append("A")
        X = a_field
    else:
        ans.append("B")
        X = a_field

    score_sum += max(a_score, b_score)

for ab in ans:
    print(ab)

print(score_sum, file=stderr)
