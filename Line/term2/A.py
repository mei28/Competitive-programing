def rnd():
    global state
    state = (state * 1564328749 + 12345) % (2**31)
    return state


def make_A():
    A = [-1 for i in range(N)]
    for i in range(N):
        A[i] = (rnd() % MAXA) + 1
    return A


def make_command():
    commands = [-1 for i in range(Q)]
    global state
    for idx in range(Q):
        if rnd() < THRESHOLD:
            l = rnd() % N
            r = rnd() % N
            v = (rnd() % MAXV) + 1

            # if l > r:
            #     tmp = r
            #     r = l
            #     l = tmp
            tmp = min(l, r)
            r = max(l, r)
            l = tmp

            commands[idx] = ("B", l, r, v)
        else:
            i = rnd() % N
            x = (rnd() % MAXA) + 1
            commands[idx] = ("A", i, x)
    return commands


def solveA(A, commands):
    i, x = commands[0], commands[1]
    A[i] = x
    return A


def solveB(A, commands):
    l, r, v = commands[0], commands[1], commands[2]
    tmp = A.copy()[l : r + 1]
    tmp = list(map(lambda x: x % v, A))
    return A, tmp.count(0)
    # cnt = 0
    # for i in tmp:
    #     if i % v == 0:
    #         cnt += 1

    # return A, cnt


def solve(A, commands):
    ans = 0
    for i in commands:
        if i[0] == "A":
            A = solveA(A, i[1:])
        else:
            A, cnt = solveB(A, i[1:])
            ans += cnt
    return ans


N, Q = map(int, input().split())
MAXA, MAXV = map(int, input().split())
SEED, THRESHOLD = map(int, input().split())

state = SEED
A = make_A()
commands = make_command()
print(solve(A, commands))
