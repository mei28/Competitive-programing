n: int = int(input())


def dfs(s: str, mx):
    if len(s) == n:
        print(s)
        return

    for i in range(ord("a"), ord(mx) + 1):
        dfs(s + chr(i), chr(ord(mx) + 1) if chr(i) == mx else mx)


dfs("", "a")
