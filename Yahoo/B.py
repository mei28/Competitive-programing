import numpy as np


def return_index(book_pena, k):
    indexs = []
    for i, v in enumerate(book_pena):
        if v < k-1:
            indexs.append(i)
    return indexs


def reset_pena(book_pena):
    book_pena_ = book_pena.copy()
    for i, v in enumerate(book_pena_):
        if v > 0:
            book_pena_[i] -= 1
        else:
            book_pena_[i] = 0
    return book_pena_


n, k = map(int, input().split())
lines = []
for i in range(n):
    line = input()
    lines.append(line)

book = [0 for _ in range(n+1)]
book = np.array(book)
book_pena = [0 for _ in range(n+1)]
for i, line in enumerate(lines):
    i = i + 1
    if 'buy' in line:
        com, num = line.split()
        book[i] = num
        print(num)
    else:
        book_index = return_index(book_pena, k)
        read_book = book[book_index]
        max_num = max(read_book)
        max_index = np.argmax(read_book)
        book_pena = reset_pena(book_pena)
        book_pena[max_index] += 1
        print(max_num)
