with open("ejdict-hand-utf8.txt", "r") as f:
    data = f.read().splitlines()

__data = set()


def is_all_alpha(word: str):
    return word.isalpha()


for i in data:
    s = i.split("\t")[0]
    s = s.lower()

    if len(s) == 5 and is_all_alpha(s):
        __data.add(s)

__data = list(__data)
__data.sort()

with open("words.txt", "w") as f:
    for i in __data:
        f.write(f"{i}\n")
