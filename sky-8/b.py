import random
import string


def generate_random_word(length):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


def generate_test_case(reserved_count, query_count, max_query_value):
    reserved_words = set()
    while len(reserved_words) < reserved_count:
        word_length = random.randint(1, 10)  # 予約語の長さを1から10の間でランダムに選ぶ
        reserved_words.add(generate_random_word(word_length))

    queries = random.sample(range(1, max_query_value + 1), query_count)

    with open("large_test_case.txt", "w") as file:
        file.write(f"{reserved_count}\n")
        for word in reserved_words:
            file.write(f"{word}\n")
        file.write(f"{query_count}\n")
        for query in queries:
            file.write(f"{query} ")
        file.write("\n")


# パラメータ：予約語の数、クエリの数、クエリの最大値
generate_test_case(1000, 2000000, 2000000)
