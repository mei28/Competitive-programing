N, M = map(int, input().split())
products = []
for _ in range(N):
    data = list(map(int, input().split()))
    P, C = data[0], data[1]
    F = set(data[2:])
    products.append((P, F))

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        pi = products[i][0]
        fi = products[i][1]

        pj = products[j][0]
        fj = products[j][1]
        if pi >= pj and fi.issubset(fj):
            if pi > pj or not fj.issubset(fi):
                print("Yes")
                exit()
print("No")
