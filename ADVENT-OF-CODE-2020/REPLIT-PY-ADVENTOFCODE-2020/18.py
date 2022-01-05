class B: 
    def __init__(self, a): self.a = a 
    def __add__(self, o):  return B(self.a + o.a)
    def __sub__(self, o):  return B(self.a * o.a)    
    def val(self):         return self.a 

f=open('18.txt')
S = 0
for l in f:
    out = ""
    for elm in l:
        if elm >='0' and elm <='9':  out+=("B("+elm+")")
        elif elm=="*":               out+= "-"
        else:                        out+=elm
    S += eval(out).a
print (S)    
f.close()
f=open('18.txt')
class A: 
    def __init__(self, a): self.a = a 
    def __add__(self, o):  return A(self.a * o.a)
    def __mul__(self, o):  return A(self.a + o.a)
    def val(self):         return self.a 
S = 0
for l in f:
    out = ""
    for elm in l:
        if elm >='0' and elm <='9':  out+=("A("+elm+")")
        elif elm=='+':               out+= "*"
        elif elm=="*":               out+= "+"
        else:                        out+=elm
    S += eval(out).a
print (S)    
f.close()

##AOC 2020 Day 18
##7147789965219
##136824720421264