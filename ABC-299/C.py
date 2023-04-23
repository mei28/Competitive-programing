n = int(input())
S = input()
rev_S = S[::-1]


# def max_dango_level(S: str) -> int:
#     N = len(S)
#     max_level = 0
#
#     i = 0
#     while i < N:
#         count_o = 0
#         if S[i] == "-":
#             i += 1
#             while i < N and S[i] == "o":
#                 count_o += 1
#                 i += 1
#             max_level = max(max_level, count_o)
#         else:
#             while i < N and S[i] == "o":
#                 count_o += 1
#                 i += 1
#             max_level = max(max_level, count_o - 1)
#
#     return max_level if max_level > 0 else -1


def max_dango_level(S: str) -> int:
    N = len(S)
    max_level = -1

    for i in range(N - 1):
        if S[i] == "o" and S[i + 1] == "-":
            count_o = 1
            while i > 0 and S[i - 1] == "o":
                count_o += 1
                i -= 1
            max_level = max(max_level, count_o)

    return max_level


ans = max_dango_level(S)
ans = max(ans, max_dango_level(rev_S))
print(ans)
