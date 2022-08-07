n = int(input())
P = [-1, -1] + list(map(int, input().split()))

now = P[n]
cnt = 0
while True:
    if now == -1:
        break
    now = P[now]
    cnt +=1

print(cnt)
