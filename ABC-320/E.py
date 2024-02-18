from collections import deque

N, M = map(int, input().split())

# 人々の列を管理するキュー
queue = deque([i for i in range(1, N + 1)])

# 各人が得たそうめんの量を保存する配列
somen = [0] * (N + 1)

events = []

for _ in range(M):
    T, W, S = map(int, input().split())
    events.append((T, "flow", W))  # そうめんが流されるイベント
    events.append((T + S, "return", queue[0]))  # 人が列に戻るイベント

# イベントを時系列順にソート
events.sort()

for event in events:
    T, event_type, *rest = event
    if event_type == "flow" and queue:
        W = rest[0]
        person = queue.popleft()  # そうめんを得る人
        somen[person] += W
    elif event_type == "return":
        person = rest[0]  # 戻る人の番号
        queue.appendleft(person)  # 人を列の先頭に戻す

for i in range(1, N + 1):
    print(somen[i])
