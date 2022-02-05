n = int(input())
A = list(map(int,input().split()))

S = [0]
for a in A:
    t = (S[-1]+a) % 360
    S.append(t)

S.sort()

ans = 0

for i in range(len(S)):
    if S[i]==S[-1]:
        ans = max(ans,360-S[i])
    else:
        ans = max(ans, S[i+1]-S[i])

print(ans)

