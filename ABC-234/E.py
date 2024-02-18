from collections import deque

x = int(input())

que = deque(range(1, 100))

while que:
    num = que.popleft()

    if num >= x:
        print(num)
        exit()

    if num >= 10:
        nf = num % 10
        ns = (num // 10) % 10
        d = nf - ns
        t = nf + d
        if 0 <= t <= 9:
            que.append(num * 10 + t)
