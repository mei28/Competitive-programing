n, q  = map(int,input().split())
s = input()
count1 = [0] * (n + 1)
count2 = [0] * (n + 1)
count_slash = [0] * (n + 1)
for i in range(n):
    count1[i + 1] = count1[i] + (1 if s[i] == '1' else 0)
    count2[i + 1] = count2[i] + (1 if s[i] == '2' else 0)
    count_slash[i + 1] = count_slash[i] + (1 if s[i] == '/' else 0)
for _ in range(q):
    l, r = map(int, input().split())
    total_1 = count1[r] - count1[l - 1]
    total_2 = count2[r] - count2[l - 1]
    total_slash = count_slash[r] - count_slash[l - 1]
    m = min(total_1, total_2, total_slash)
    if m > 0:
        print(2 * m + 1)
    else:
        print(0)

