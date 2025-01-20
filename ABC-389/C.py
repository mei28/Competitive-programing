from collections import deque

q = int(input())

queue = deque()
offset = 0  # 現在の全体オフセット（タイプ2による移動を効率的に処理）

results = []

for i in range(q):
    query = input().split()
    type_query = int(query[0])

    if type_query == 1:
        l = int(query[1])
        head_position = queue[-1][1] + queue[-1][0] if queue else 0
        queue.append((l, head_position))

    elif type_query == 2:
        m = queue.popleft()[0]
        offset += m

    elif type_query == 3:
        k = int(query[1]) - 1
        length, original_position = queue[k]
        results.append(str(original_position - offset))


for result in results:
    print(result)
