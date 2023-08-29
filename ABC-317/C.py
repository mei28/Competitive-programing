N, M = map(int, input().split())

# 隣接リストの初期化
adj_list = [[] for _ in range(N)]

# 道路情報を読み取り、隣接リストを作成
for _ in range(M):
    A, B, C = map(int, input().split())
    adj_list[A - 1].append((B - 1, C))
    adj_list[B - 1].append((A - 1, C))


# DFSを使って最大経路長を計算
def dfs(current, visited, total_length):
    visited[current] = True
    max_length = total_length

    for next_city, length in adj_list[current]:
        if not visited[next_city]:
            max_length = max(
                max_length, dfs(next_city, visited[:], total_length + length)
            )

    return max_length


max_route_length = 0

for city in range(N):
    max_route_length = max(max_route_length, dfs(city, [False] * N, 0))

print(max_route_length)
