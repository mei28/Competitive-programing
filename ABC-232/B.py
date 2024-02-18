S = input()
T = input()

k = (ord(T[0]) - ord(S[0])) % 26


def rot_n(s, n):
    answer = ""
    for letter in s:
        answer += chr(ord("a") + (ord(letter) - ord("a") + n) % 26)

    return answer


_S = rot_n(S, k)

if _S == T:
    print("Yes")

else:
    print("No")
# print(k)
# for s,t in zip(S,T):
#     tmp = (ord(T[0])- ord(S[0])) %26
#     print(k,tmp)
#     if tmp != k:
#         print("No")
#         exit()

# print('Yes')
