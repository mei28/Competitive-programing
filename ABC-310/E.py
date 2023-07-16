def solve(N, S):
    # Initialize a list to keep track of the distance to the next 1 in S
    next_one = [0] * N
    distance = N  # The initial distance can be any value >= N

    # Calculate distances to the next 1 in S, from right to left
    for i in range(N - 1, -1, -1):
        if S[i] == "1":
            distance = 0
        next_one[i] = distance
        distance += 1

    # Initialize the result and the number of continuous 0s from the left
    res = cnt_zero = 0
    for i in range(N):
        if S[i] == "0":
            cnt_zero += 1
        else:
            cnt_zero = 0
        res += min(cnt_zero, next_one[i])
    return res


N = int(input().strip())
S = input().strip()
print(solve(N, S))
