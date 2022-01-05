#this one might need to be reused for coming days... ;-(

h=open("16.TXT","rt").read().strip() # hex
b=''.join(('000'+bin(int(x,16))[2:])[-4:] for x in h)
p=0 # position in b (bits)

def get(n):
  global p
  r=int(b[p:p+n],2)
  p+=n
  return r

a=0 # version accumulator

def decode():
  global a
  v=get(3) # version
  a+=v
  t=get(3) # type id
  if t==4: # literals
    c=get(1) # continue
    d=get(4) # digit
    r=d
    while c:
      c=get(1) # continue
      d=get(4) # digit
      r=16*r+d
  else: # operator
    s=[] # sub-packets
    i=get(1) # length type id
    if i: # # of sub-packets
      q=get(11) # quantity
      for _ in range(q):
        s.append( decode() )
    else: # # of bits
      l=get(15) # length
      e=p+l # end
      while p<e:
        s.append( decode() )
    if t==0: r=sum(s)
    elif t==1: # prod
      r=1
      for x in s:
        r*=x
    elif t==2: r=min(s)
    elif t==3: r=max(s)
    elif t==5: r=int(s[0]>s[1])
    elif t==6: r=int(s[0]<s[1])
    elif t==7: r=int(s[0]==s[1])
  return r

r=decode()
print(a)
print(r)

#891
#673042777597