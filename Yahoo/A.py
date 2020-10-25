V = list(map(int, input().split()))

max_abs = -1
for i in range(1, len(V)):
    tmp_abs = abs(V[i-1]-V[i])
    max_abs = max(max_abs,tmp_abs)
tmp_abs = abs(V[0] - V[-1])
max_abs = max(max_abs,tmp_abs)
print(max_abs)