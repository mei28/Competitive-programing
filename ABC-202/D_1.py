a, b, k = map(int, input().split())
n = a + b
k -= 1
c = k // b
d = k - b * c
print(c, d)
