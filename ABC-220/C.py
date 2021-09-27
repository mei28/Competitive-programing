N = int(input())
A = list(map(int, input().split()))
X = int(input())

ans = 0  # 現在の項数
S = 0  # 現在の総和
sum_A = sum(A)

c = X // sum_A  # A全体を何回使うか
ans += c * N  # A全体を何回使うか×Aの項数
S += c * sum_A  # A全体を何回使うか×Aの総和

for a in A:
    S += a
    ans += 1
    if S > X:  # Xを超えるときなので < です
        break

print(ans)
