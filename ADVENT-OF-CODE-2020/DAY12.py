#AdventOfCode day 12, both parts

h=p=s=0
w=10+1j

for l in open("12.TXT"):
 i,x="RFLWSEN".index(l[0])-1,int(l[1:])
 if i>1:d=x*1j**i;p+=d;w+=d
 elif i:d=x*i;h+=d;w*=1j**(d/90)
 else:p+=x*1j**(h/90);s+=x*w

print(*[int(abs(z.real)+abs(z.imag))for z in(p,s)])

## 1601 13340

####    AOC 2020 Day 12
####    1601 13340
####    Loaded puzzle input from 12.txt