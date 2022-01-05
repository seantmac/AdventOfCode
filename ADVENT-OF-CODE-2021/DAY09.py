from math import prod

height = {(x,y):int(h) for y,l in enumerate(open('9.TXT'))
                       for x,h in enumerate(l.strip())}

def neighbours(x, y):
  return filter(lambda n: n in height,  # remove points
    [(x,y-1),(x,y+1),(x-1,y),(x+1,y)])  #  outside grid

def is_low(p):
  return all(height[p] < height[n]
    for n in neighbours(*p))

low_points = list(filter(is_low, height))
print(sum(height[p]+1 for p in low_points))

def count_basin(p):
  if height[p] == 9: return 0  # stop counting at ridge
  del height[p]                # prevent further visits
  return 1+sum(map(count_basin, neighbours(*p)))

basins = [count_basin(p) for p in low_points]
print(prod(sorted(basins)[-3:]))

#462
#1397760