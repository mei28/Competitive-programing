from argparse import ArgumentParser
from pdb import set_trace as pst

from itertools import permutations

with open("words.txt", "r") as f:
    data = f.read().splitlines()

data = set(data)

alp = [chr(i) for i in range(ord("a"), ord("z") + 1)]


def main(word: str):
    wild_cnt = word.count("*")
    comb: list = get_permutations(wild_cnt)
    ret = []
    for i in comb:
        if not check_include_word(i):
            continue
        _word = replace_wild(word, i)
        if check_in_data(_word):
            ret.append(_word)
    print(*ret)


def replace_wild(word: str, comb: list):
    for i in comb:
        word = word.replace("*", i, 1)
    return word


def check_in_data(word: str):
    return word in data


def get_permutations(n: int) -> list:

    _alp = alp
    if args.exclude_word:
        _alp = list(set(alp) - set(args.exclude_word))
    return list(permutations(_alp, n))


def check_include_word(candidate_word: str):
    include_word = args.include_word
    if include_word is None:
        return True
    return any([i in include_word for i in candidate_word])


def get_args():
    parser = ArgumentParser()
    parser.add_argument("--word", "-w", type=str, required=True)
    parser.add_argument("--exclude_word", "-ew", type=str)
    parser.add_argument("--include_word", "-iw", type=str)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = get_args()
    main(args.word)
