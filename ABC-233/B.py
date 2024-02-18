l, r = map(int, input().split())
l -= 1
r -= 1
S = input()
print(S[:l] + S[l : r + 1][::-1] + S[r + 1 :])
