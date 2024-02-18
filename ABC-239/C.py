x1, y1, x2, y2 = map(int, input().split())

# d = (x1-x2)**2 + (y1-y2)**2

# if d<=20:
#     print('Yes')
# else:
#     print('No')

dx = [1, -1, -2, -2, -1, 1, 2, 2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]

for i in range(8):
    for j in range(8):
        if x1 + dx[i] == x2 + dx[j] and y1 + dy[i] == y2 + dy[j]:
            print("Yes")
            exit()

print("No")
