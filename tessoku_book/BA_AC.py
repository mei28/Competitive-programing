pq = []

INF = 10**10

Q = int(input())


def parent(x):
    return (x - 1) // 2


def left(x):
    return x * 2 + 1


def right(x):
    return x * 2 + 2


for _ in range(Q):
    query = list(input().split())
    if query[0] == "1":
        x = int(query[1])
        pq.append(x)
        now = len(pq) - 1
        while now > 0 and pq[parent(now)] > pq[now]:
            pq[parent(now)], pq[now] = pq[now], pq[parent(now)]
            now = parent(now)
    if query[0] == "2":
        print(pq[0])
    if query[0] == "3":
        if len(pq) == 1:
            pq = []
            continue
        pq[0] = pq.pop()
        now = 0
        while True:
            l = left(now)
            r = right(now)
            lValue = pq[l] if l < len(pq) else INF
            rValue = pq[r] if r < len(pq) else INF
            nowValue = pq[now]
            # both OK
            if nowValue <= lValue and nowValue <= rValue:
                break
            # r NG
            if nowValue <= lValue:
                pq[now], pq[r] = pq[r], pq[now]
                now = r
            # l NG
            if nowValue <= rValue:
                pq[now], pq[l] = pq[l], pq[now]
                now = l
            # both NG, l <= r
            if lValue <= rValue:
                pq[now], pq[l] = pq[l], pq[now]
                now = l
            # both NG, r < l
            else:
                pq[now], pq[r] = pq[r], pq[now]
                now = r
