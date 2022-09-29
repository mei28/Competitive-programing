n = int(input())
A = list(map(int, input().split()))
B = [0] * 5
tcd = [-1, 20, 40, 60, 80, 100]
for a in A:
    for i in range(5):
        if tcd[i] < a <= tcd[i + 1]:
            B[i] += 1
print(*B)
