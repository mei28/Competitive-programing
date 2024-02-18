N = int(input())
S = input()

max_size = 0
for i in range(1, N):
    left = set(S[:i])
    right = set(S[i:])
    all_ = left & right
    max_size = max(max_size, len(all_))

print(max_size)
