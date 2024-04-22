def word_to_index(word: str) -> int:
    index = 0
    for char in word:
        index = index * 26 + (ord(char) - ord("a"))
    return index


def index_to_word(index: int) -> str:
    result = []
    while index >= 0:
        result.append(chr((index % 26) + ord("a")))
        index = index // 26 - 1
    return "".join(result[::-1])


def find_nth_non_reserved(n: int, reserved_indices: list) -> str:
    current_index = 0
    count = 0

    for reserved_index in reserved_indices:
        if reserved_index > current_index:
            non_reserved_count = reserved_index - current_index
            if count + non_reserved_count >= n:
                return index_to_word(current_index + (n - count) - 1)
            count += non_reserved_count
        current_index = reserved_index + 1

    return index_to_word(current_index + (n - count) - 1)


n = int(input())
S = [input() for _ in range(n)]
q = int(input())
query = list(map(int, input().split()))

reserved_indices = [word_to_index(word) for word in S]
reserved_indices.sort()

for q in query:
    print(find_nth_non_reserved(q, reserved_indices), end=" ")
