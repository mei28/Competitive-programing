N = int(input())
A = list(map(int, input().split()))
a = max(A)
B = list(map(int, input().split()))
b = min(B)

print(max(0, b - a + 1))
