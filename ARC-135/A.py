x = int(input())
MOD = 998244353


M = dict()


def dfs(_x: int) -> int:
    if _x in M.keys():
        return M[_x]
    if _x < 4:
        return _x

    M[_x] = (dfs(_x // 2) * dfs(-(-_x // 2))) % MOD
    return M[_x]


print(dfs(x))
