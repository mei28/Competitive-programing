import itertools


def is_palindrome(substring):
    return substring == substring[::-1]


def contains_k_palindrome(s, k):
    for i in range(len(s) - k + 1):
        if is_palindrome(s[i : i + k]):
            return True
    return False


def count_valid_permutations(s, k):
    unique_permutations = set(itertools.permutations(s))
    count = 0
    for perm in unique_permutations:
        perm_str = "".join(perm)
        if not contains_k_palindrome(perm_str, k):
            count += 1
    return count


N, K = map(int, input().split())
S = input()

result = count_valid_permutations(S, K)
print(result)
