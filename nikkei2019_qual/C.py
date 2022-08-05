n = int(input())
A, B = [], []
AB = []

for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    AB.append(a+b)

AB.sort(reverse=True)
ans = -(sum(B))
for i in range((n+2-1)//2):
    ans += AB[i*2]

print(ans)
