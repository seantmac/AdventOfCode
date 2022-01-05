"""Day 23 of Advent of Code 2020 Solution"""
 
 
def cup_io(file_location):
    with open(file_location, "r") as f:
        cups = [int(i) for i in f.readline().strip()]
    return cups
 
 
class CrabCups:
    def __init__(self, cups):
        self.current = cups[0]
        self.next_cup = {}
        for i, c in enumerate(cups, 1):
            try:
                self.next_cup[c] = cups[i]
            except IndexError:
                self.next_cup[c] = cups[0]
 
    def __iter__(self):
        return self
 
    def __next__(self):
        remove = []
        to_move = self.current
        for i in range(3):
            remove.append(self.next_cup[to_move])
            to_move = self.next_cup[to_move]
        self.next_cup[self.current] = self.next_cup[remove[2]]
        destination = self.current - 1
        while destination <= 0 or destination in remove:
            if destination == 0:
                destination = len(self.next_cup)
            if destination in remove:
                destination -= 1
        self.next_cup[destination], self.next_cup[remove[2]] = (
            remove[0],
            self.next_cup[destination],
        )
        self.current = self.next_cup[self.current]
 
    @property
    def final(self):
        current = 1
        output = []
        for _ in range(len(self.next_cup) - 1):
            output.append(self.next_cup[current])
            current = self.next_cup[current]
        output = [str(n) for n in output]
        return "".join(output)
 
 
def part1(file_location):
    cups = cup_io(file_location)
    cc = CrabCups(cups)
    for _ in range(100):
        next(cc)
    return cc.final
 
 
def part2(file_location):
    cups = cup_io(file_location)
    cups.extend(range(10, 1000001))
    cc = CrabCups(cups)
    for i in range(10000000):
        next(cc)
    a = cc.next_cup[1]
    b = cc.next_cup[a]
    return a * b
 
 
if __name__ == "__main__":
    file_location = "23.txt"
    print("A  ", part1(file_location))
    print("B  ", part2(file_location))


    
    ##A      62934785
    ##B      693659135400