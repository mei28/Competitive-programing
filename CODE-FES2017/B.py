n = int(input())
A = list(map(int, input().split()))

k = 1

for a in A:
    if a % 2 == 0:
        k *= 2
print(3**n - k)
