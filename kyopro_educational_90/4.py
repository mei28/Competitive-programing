H, W = map(int, input().split())
mat = [] * H

for _ in range(H):
    row = list(map(int, input().split()))
    mat.append(row)

rows = [] * H
cols = [0] * W

for row in mat:
    rows.append(sum(row))
    for j in range(W):
        cols[j] += row[j]

for r in range(H):
    for c in range(W):
        print(rows[r] + cols[c] - mat[r][c], end=" ")
    print()
