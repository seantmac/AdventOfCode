from os import path
import re

REQUIREMENTS = [
    ("byr", lambda x: 1920 <= int(x) <= 2002),
    ("iyr", lambda x: 2010 <= int(x) <= 2020),
    ("eyr", lambda x: 2020 <= int(x) <= 2030),
    ("hgt", lambda x: (x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193) or (x[-2:] == "in" and 59 <= int(x[:-2]) <= 76)),
    ("hcl", lambda x: re.fullmatch(r"#[0-9a-f]{6}", x)),
    ("ecl", lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")),
    ("pid", lambda x: re.fullmatch(r"[0-9]{9}", x)),
]


##   byr (Birth Year)
##   iyr (Issue Year)
##   eyr (Expiration Year)
##   hgt (Height)
##   hcl (Hair Color)
##   ecl (Eye Color)
##   pid (Passport ID)
##   cid (Country ID)

##   ugly data...
##   hgt:168cm eyr:2026 ecl:hzl hcl:#fffffd cid:169 pid:920076943
##   byr:1929 iyr:2013
##
##   hgt:156cm ecl:brn eyr:2023
##   iyr:2011
##   hcl:#6b5442 pid:328412891 byr:1948
##
##   byr:1950 iyr:2019 eyr:2020 ecl:amb cid:279 pid:674907993 hgt:189cm hcl:#602927
##
##   byr:1976
##   ecl:hzl iyr:2015 hgt:178cm eyr:2022 hcl:#341e13
##   pid:473630095


with open(path.join(path.dirname(__file__), "04.txt")) as f:
    part1 = part2 = 0

    for passport_lines in f.read().split("\n\n"):
        passport = {}

        for line in passport_lines.splitlines():
            for parts in line.split():
                key, value = parts.split(":")
                passport[key] = value

        valid1 = valid2 = True

        for key, req in REQUIREMENTS:
            if key not in passport:
                valid1 = False
                break
            if not req(passport[key]):
                valid2 = False

        if valid1:
            part1 += 1
            part2 += valid2

    print("Part 1:", part1)
    print("Part 2:", part2)

    ## Part1: 190
    ## Part2: 121


##    AOC 2020 Day 4
##    Part 1: 190
##    Part 2: 121
##    Loaded puzzle input from 04.txt