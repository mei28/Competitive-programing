MOD = 998244353


def process_queries(queries):
    s = [1]
    acc_mod = [0] * (len(queries) + 1)
    acc_mod[0] = 1

    for query in queries:
        if query[0] == 1:
            s.append(query[1])
            acc_mod[len(s) - 1] = (acc_mod[len(s) - 2] * 10) % MOD
        elif query[0] == 2:
            s.pop()
        elif query[0] == 3:
            result = 0
            for i, digit in enumerate(s):
                result += digit * acc_mod[len(s) - 1 - i]
                result %= MOD
            print(result)


def main():
    q = int(input())
    queries = []
    for _ in range(q):
        query = list(map(int, input().split()))
        queries.append(query)

    process_queries(queries)


if __name__ == "__main__":
    main()
