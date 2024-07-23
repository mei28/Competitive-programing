from collections import deque

def bfs(sea_level, visited, A, H, W, queue):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and A[nx][ny] <= sea_level:
                visited[nx][ny] = True
                queue.append((nx, ny))

def simulate_sea_level_rise(H, W, A, Y):
    remaining_land_areas = []
    visited = [[False] * W for _ in range(H)]
    queue = deque()

    
    for i in range(H):
        for j in range(W):
            if (i == 0 or i == H-1 or j == 0 or j == W-1) and A[i][j] <= 0:
                visited[i][j] = True
                queue.append((i, j))

    for year in range(1, Y + 1):
        sea_level = year
        bfs(sea_level, visited, A, H, W, queue)

        remaining_land = sum(1 for i in range(H) for j in range(W) if not visited[i][j])
        remaining_land_areas.append(remaining_land)

    return remaining_land_areas


H, W, Y = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]


result = simulate_sea_level_rise(H, W, A, Y)


for area in result:
    print(area)

