
n = int(input())
a = list(map(int, input().split()))

x = a[-1]
for i in range(n - 1):
    if a[i] > a[i + 1]:
        x = a[i]
        break

a = [v for v in a if v != x]
print(*a)
