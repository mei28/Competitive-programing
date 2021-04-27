N = int(input())
S = input()

cum_sum_w = [0] * (N + 1)
cum_sum_e = [0] * (N + 1)
answers = [0] * N
for i in range(N):
    if S[i] == "W":
        tmp = 1
    else:
        tmp = 0
    cum_sum_w[i + 1] = cum_sum_w[i] + tmp
for i in range(N):
    if S[i] == "E":
        tmp = 1
    else:
        tmp = 0
    cum_sum_e[i + 1] = cum_sum_e[i] + tmp
for i in range(N):
    answers[i] = cum_sum_w[i] + (cum_sum_e[N] - cum_sum_e[i + 1])
print(min(answers))
