n, m = map(int, input().split())
K, S = [], []

for i in range(m):
    t = list(map(int, input().split()))
    K.append(t[0])
    S.append(list(map(lambda x: x - 1, t[1:])))

P = list(map(int, input().split()))


ans = 0
for bits in range(1 << n):
    on_switch = []
    off_switch = []
    on_light = 0
    for j in range(n):
        if (bits >> j) & 1:
            on_switch.append(j)
        else:
            off_switch.append(j)
    # 点灯しているライトを数える
    for i in range(m):
        cnt = 0
        tmp = set(on_switch) & set(S[i])
        if len(tmp) % 2 == P[i]:
            on_light += 1
    if on_light == m:
        ans += 1
print(ans)
