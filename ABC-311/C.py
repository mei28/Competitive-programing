N = int(input())
A = list(map(int, input().split()))

# 頂点は0-indexedとする
A = [a - 1 for a in A]

visited = [False] * N  # 訪問フラグ
cycle = []  # 閉路
pos = 0  # 現在地

# DFSで閉路を探す
while True:
    if visited[pos]:
        cycle_start = cycle.index(pos)
        cycle = cycle[cycle_start:]
        break
    else:
        visited[pos] = True
        cycle.append(pos)
        pos = A[pos]

# 閉路を表示（頂点は1-indexedで表示）
print(len(cycle))
for v in cycle:
    print(v + 1, end=" ")
