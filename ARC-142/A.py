N, K = map(int, input().split())
k = K

ans = set()

while k <= N:
    ans.add(k)
    k *= 10

k = int(str(K)[::-1])
while k <= N:
    ans.add(k)
    k *= 10

# print(ans)
if K > int(str(K)[::-1]):
    print(0)
else:
    print(len(ans))
