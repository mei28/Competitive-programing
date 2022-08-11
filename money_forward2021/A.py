import sys


def num2words(num):
    nums_20_90 = [
        "Twenty",
        "Thirty",
        "Forty",
        "Fifty",
        "Sixty",
        "Seventy",
        "Eighty",
        "Ninety",
    ]
    nums_0_19 = [
        "Zero",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
    ]
    nums_dict = {
        100: "hundred",
        1000: "thousand",
        1000000: "million",
        1000000000: "billion",
    }
    if num < 20:
        return nums_0_19[num]
    if num < 100:
        return nums_20_90[num // 10 - 2] + (
            "" if num % 10 == 0 else " " + nums_0_19[num % 10]
        )
    # find the largest key smaller than num
    maxkey = max([key for key in nums_dict.keys() if key <= num])
    return (
        num2words(num // maxkey)
        + " "
        + nums_dict[maxkey]
        + ("" if num % maxkey == 0 else " " + num2words(num % maxkey))
    )


def float2words(num: str) -> str:
    if num == "":
        return ""
    num_str: str = num
    dct = {
        "0": "zero ",
        "1": "one ",
        "2": "two ",
        "3": "three ",
        "4": "four ",
        "5": "five ",
        "6": "six ",
        "7": "seven ",
        "8": "eight ",
        "9": "nine ",
    }
    ret = " point "

    for c in num_str:
        ret += dct[c]
    return ret


def convert(a: str, b: str) -> str:
    ret: str = a + b
    ret = ret.lower()
    head_word = ret.split(" ")[0][0].upper() + ret.split(" ")[0][1:]
    other_words = ret.split(" ")[1:]
    ret = head_word + " "
    for w in other_words:
        ret += w + " "
    return ret


def main(lines):
    num_seisu: int = int(float(lines[0]))
    if "." in lines[0]:
        num_syousu = lines[0].split(".")[1]
    else:
        num_syousu = ""
    seisu_str: str = num2words(num_seisu)
    syousu_str: str = float2words(num_syousu)
    print(convert(seisu_str, syousu_str))


if __name__ == "__main__":
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip("\r\n"))
    main(lines)
