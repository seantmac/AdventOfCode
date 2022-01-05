#!/usr/bin/python

with open('25.TXT', 'r') as f:
    pk_card = int(f.readline())
    pk_door = int(f.readline())


    loopsize_card = 0
    num = 1
    while num != pk_card:
        num = (num * 7) % 20201227
        loopsize_card += 1
    print(f'Card loop size: {loopsize_card}')

    loopsize_door = 0
    num = 1
    while num != pk_door:
        num = num * 7 % 20201227
        loopsize_door += 1
    print(f'Door loop size: {loopsize_door}')

    num = 1
    for i in range(loopsize_card):
        num = num * pk_door % 20201227
    print(f'Part 1: {num} (card -> door)')

    num = 1
    for i in range(loopsize_door):
        num = num * pk_card % 20201227
    print(f'Part 1: {num} (card -> door)')

#AOC 2020 Day 25
#Card loop size: 1063911
#Door loop size: 1388395
#Part 1: 290487 (card -> door)
#Part 1: 290487 (card -> door)
#Loaded puzzle input from 25.txt