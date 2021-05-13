N = int(input())
A = list(map(int, input().split()))

if sum(A) / len(A) < 0:
    ave = int((sum(A)) / len(A) - 0.5)
else:
    ave = int((sum(A)) / len(A) + 0.5)

ans = sum(map(lambda x: (x - ave) ** 2, A))
print(ans)
