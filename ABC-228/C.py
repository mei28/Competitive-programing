n, k = map(int, input().split())
s = [0] * n
for i in range(n):
    s[i] = sum(map(int, input().split()))
t = sorted(s, reverse=True)[k - 1]
for x in s:
    print("Yes" if x + 300 >= t else "No")
