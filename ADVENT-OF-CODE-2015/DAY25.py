R = 3010
C = 3019

def f(x):
  return (x*252533)%33554393

v = 20151125
r,c = 1,1

while True:
  if r == R and c == C:
    break
  r -= 1
  c += 1
  if r == 0:
    r = c
    c = 1
  v = f(v)

print("1  ", v)

#8997277