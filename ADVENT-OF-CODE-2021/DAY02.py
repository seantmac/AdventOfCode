with open('2.TXT', 'r', encoding='utf-8') as inst_file:
   instructions = [inst_line.strip().split(" ") for inst_line in inst_file.readlines()]
forward = sum(int(il[1]) for il in instructions if il[0] == "forward")
depth = sum(int(il[1]) if il[0] == "down" else -int(il[1]) for il in instructions if il[0] != "forward")
print("Part 1: Horizontal: {}, depth: {}, multiplied: {}".format(forward, depth, forward*depth))

depth, forward, aim = 0, 0, 0
for il in instructions:
   inst_val = int(il[1])
   match il[0]:
      case "up":
         aim -= inst_val
      case "down":
         aim += inst_val
      case "forward":
         forward += inst_val
         depth += inst_val*aim
print("Part 2: Horizontal: {}, depth: {}, multiplied: {}".format(forward, depth, forward*depth))

##   Part 1: Horizontal: 1998, depth: 741, multiplied: 1480518
##   Part 2: Horizontal: 1998, depth: 642047, multiplied: 1282809906
