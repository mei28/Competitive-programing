N = int(input())


ans = set()
ans.add(1)
for i in range(1,N):
    if i*i>N:
        break

    if N%i==0:
        ans.add(i)
        ans.add(N//i)

ans = list(ans)
ans = sorted(ans)

for i in ans:
    print(i)