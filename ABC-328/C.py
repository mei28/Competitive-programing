n, q = map(int, input().split())
s = input()
lr = [map(int, input().split()) for _ in range(q)]


cumulative_counts = [0] * (len(s) + 1)
for i in range(1, len(s)):
    cumulative_counts[i + 1] = cumulative_counts[i] + (s[i] == s[i - 1])

for l, r in lr:
    count = cumulative_counts[r] - cumulative_counts[l]
    print(count)
