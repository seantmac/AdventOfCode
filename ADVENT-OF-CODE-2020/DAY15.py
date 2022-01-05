def solution(numbers, until=2020):
    memory = {n: i + 1 for i, n in enumerate(numbers[:-1])}

    for i in range(len(numbers), until):
        numbers.append(i - memory.get(numbers[-1], i))
        memory[numbers[-2]] = i

    return numbers[-1]


##numbers = [2,0,6,12,1,3]
numbers = [int(x) for x in open("15.TXT").read().split(",")]
print(f"Solution part 1: {solution(numbers)}")
print(f"Solution part 2: {solution(numbers, 30000000)}")


## Solution part 1: 1428
## Solution part 2: 3718541


## AOC 2020 Day 15
## Solution part 1: 1428
## repl process died unexpectedly: signal: killed