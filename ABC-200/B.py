N, K = map(int, input().split())


def query(q: int):
    if q % 200 == 0:
        q //= 200
    else:
        q = int(str(q) + "200")
    return q


for i in range(K):
    N = query(N)
print(N)
