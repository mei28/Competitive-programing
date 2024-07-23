from collections import Counter


def is_palindrome(s):
    return s == s[::-1]


def count_valid_permutations(n, k, S):
    count = Counter(S)

    def permute(counter, prefix):
        if len(prefix) == n:
            for i in range(n - k + 1):
                if is_palindrome(prefix[i : i + k]):
                    return False
            return True

        for char in list(counter):
            if counter[char] > 0:
                counter[char] -= 1
                if permute(counter, prefix + char):
                    valid_permutations.add(prefix + char)
                counter[char] += 1

    valid_permutations = set()
    permute(count, "")

    return len(valid_permutations)


n, k = map(int, input().split())
S = input()

print(count_valid_permutations(n, k, S))
