def max_binary_under_N(S, N):
    # Replace '?' with '1'
    S = S.replace("?", "1")
    num = int(S, 2)

    if num <= N:
        return num

    # Replace '1' with '0' from the highest bit
    for i in range(len(S) - 1, -1, -1):
        if S[i] == "1":
            S = S[:i] + "0" + S[i + 1 :]
            num = int(S, 2)
            if num <= N:
                return num

    return -1


# Input example
S = input()
N = int(input())
print(max_binary_under_N(S, N))  # Output: 1
