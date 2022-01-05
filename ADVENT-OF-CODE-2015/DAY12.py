import json
import re


def sum_numbers(s):
    return sum(int(i) for i in re.findall(r"(-?\d+)", str(s)))


def sum_non_reds(s):
    if isinstance(s, int):
        return s
    elif isinstance(s, list):
        return sum(sum_non_reds(i) for i in s)
    elif isinstance(s, dict):
        if "red" in s.values():
            return 0
        else:
            return sum(sum_non_reds(i) for i in s.values())

    return 0


def part_one():
    with open("12.TXT") as fin:
        print(sum_numbers(fin.read()))


def part_two():
    with open("12.TXT") as fin:
        print(sum_non_reds(json.load(fin)))


if __name__ == "__main__":
    part_one()
    part_two()

#119433
#68466