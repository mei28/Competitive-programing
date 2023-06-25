n = int(input())
S = [input() for _ in range(n)]


def is_palindrome(s):
    return s == s[::-1]


for i in range(n):
    for j in range(n):
        if i == j:
            continue
        combined_string = S[i] + S[j]
        if is_palindrome(combined_string):
            print("Yes")
            exit()
print("No")
