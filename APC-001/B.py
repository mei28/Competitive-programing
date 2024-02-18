n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt_A = 0
cnt_B = 0

for a, b in zip(A, B):
    if a > b:
        cnt_A += a - b
    elif b > a:
        cnt_B += (b - a) // 2

print("Yes") if cnt_B >= cnt_A else print("No")
