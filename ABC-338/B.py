from collections import Counter

s = input()
cnt = Counter(s)


def most_common_char(S):
    counts = Counter(S)

    max_count = max(counts.values())

    most_common_chars = sorted(
        [char for char, count in counts.items() if count == max_count]
    )

    return most_common_chars[0]


print(most_common_char(s))
